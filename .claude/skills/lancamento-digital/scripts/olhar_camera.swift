// Lista trechos em que o rosto nao esta virado para a camera. So funciona no macOS.
// Uso: swift olhar_camera.swift video.mp4 [limite_em_graus=38] [amostras_por_segundo=6] [largura_minima_do_rosto=0.2]
// Rode na gravacao bruta, antes da edicao: cartoes e telas viram falso positivo.
// Saida: JSON com os trechos a cortar, em segundos. Tambem marca trechos sem rosto,
// entao use em gravacoes de rosto, nao em telas. O Vision arredonda o angulo em degraus,
// por isso o limite padrao e alto. Se a pessoa olha para o lado e nao aparece no JSON,
// suba a largura minima (0.36 funcionou em enquadramento fechado de celular).
import AVFoundation
import Foundation
import Vision

let args = CommandLine.arguments
guard args.count >= 2 else { print("Uso: swift olhar_camera.swift video.mp4 [graus] [fps] [largura]"); exit(2) }
let limite = (args.count > 2 ? Double(args[2]) : nil) ?? 38
let fps = (args.count > 3 ? Double(args[3]) : nil) ?? 6
let larguraMinima = (args.count > 4 ? Double(args[4]) : nil) ?? 0.2

let asset = AVURLAsset(url: URL(fileURLWithPath: args[1]))
let duracao = CMTimeGetSeconds(asset.duration)
guard duracao > 0 else { print("Nao consegui ler o video."); exit(1) }
let gerador = AVAssetImageGenerator(asset: asset)
gerador.appliesPreferredTrackTransform = true
gerador.maximumSize = CGSize(width: 640, height: 640)
gerador.requestedTimeToleranceBefore = CMTime(value: 1, timescale: 30)
gerador.requestedTimeToleranceAfter = CMTime(value: 1, timescale: 30)

var ruins: [Double] = []
var t = 0.0
while t < duracao {
    autoreleasepool {
        let tempo = CMTime(seconds: t, preferredTimescale: 600)
        guard let img = try? gerador.copyCGImage(at: tempo, actualTime: nil) else { return }
        let req = VNDetectFaceRectanglesRequest()
        req.revision = VNDetectFaceRectanglesRequestRevision3
        try? VNImageRequestHandler(cgImage: img, options: [:]).perform([req])
        let maior = (req.results ?? []).max { $0.boundingBox.width < $1.boundingBox.width }
        if let rosto = maior, let yaw = rosto.yaw?.doubleValue {
            if abs(yaw * 180 / Double.pi) >= limite || Double(rosto.boundingBox.width) < larguraMinima { ruins.append(t) }
        } else {
            ruins.append(t)
        }
    }
    t += 1 / fps
}

var trechos: [[String: Double]] = []
for x in ruins {
    if var ultimo = trechos.last, x - ultimo["fim"]! <= 1.5 / fps {
        ultimo["fim"] = x + 1 / fps
        trechos[trechos.count - 1] = ultimo
    } else {
        trechos.append(["inicio": x, "fim": x + 1 / fps])
    }
}
let saida: [String: Any] = ["duracao": duracao, "limite_graus": limite, "cortar": trechos]
let dados = try JSONSerialization.data(withJSONObject: saida, options: [.prettyPrinted, .sortedKeys])
print(String(data: dados, encoding: .utf8)!)
