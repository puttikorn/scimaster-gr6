import Foundation
import PDFKit
import Vision
import AppKit

let pdfPath = "Documents/Reading with Writing GR6-MidFinal.pdf"
let outputDir = "extracted_text_reading"

let fileManager = FileManager.default
if !fileManager.fileExists(atPath: outputDir) {
    try? fileManager.createDirectory(atPath: outputDir, withIntermediateDirectories: true)
}

guard let pdfDoc = PDFDocument(url: URL(fileURLWithPath: pdfPath)) else {
    print("Failed to load PDF: \(pdfPath)")
    exit(1)
}

let pageCount = pdfDoc.pageCount
print("Loaded PDF with \(pageCount) pages. Starting Apple Vision OCR (English + Thai)...")

var fullText = ""

for pageIndex in 0..<pageCount {
    guard let page = pdfDoc.page(at: pageIndex) else { continue }
    let pageBounds = page.bounds(for: .mediaBox)
    let scale: CGFloat = 2.0
    let targetSize = NSSize(width: pageBounds.width * scale, height: pageBounds.height * scale)
    let nsImage = page.thumbnail(of: targetSize, for: .mediaBox)
    
    var imageRect = NSRect(origin: .zero, size: nsImage.size)
    guard let cgImage = nsImage.cgImage(forProposedRect: &imageRect, context: nil, hints: nil) else {
        print("Failed to get cgImage for page \(pageIndex + 1)")
        continue
    }
    
    let requestHandler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.recognitionLanguages = ["en-US", "th-TH"]
    request.usesLanguageCorrection = true
    
    do {
        try requestHandler.perform([request])
        guard let observations = request.results else { continue }
        
        // Sort top-to-bottom, left-to-right
        let sortedObservations = observations.sorted { (a, b) -> Bool in
            let yA = a.boundingBox.origin.y
            let yB = b.boundingBox.origin.y
            if abs(yA - yB) > 0.02 {
                return yA > yB
            }
            return a.boundingBox.origin.x < b.boundingBox.origin.x
        }
        
        let recognizedStrings = sortedObservations.compactMap { $0.topCandidates(1).first?.string }
        let pageText = recognizedStrings.joined(separator: "\n")
        
        let pageFile = "\(outputDir)/page_\(pageIndex + 1).txt"
        try? pageText.write(toFile: pageFile, atomically: true, encoding: .utf8)
        
        fullText += "\n==================== PAGE \(pageIndex + 1) ====================\n"
        fullText += pageText + "\n"
        
        print("Processed Page \(pageIndex + 1)/\(pageCount) (\(recognizedStrings.count) lines)")
    } catch {
        print("OCR error on page \(pageIndex + 1): \(error)")
    }
}

let fullFile = "\(outputDir)/full_reading_ocr.txt"
try? fullText.write(toFile: fullFile, atomically: true, encoding: .utf8)
print("OCR Complete! Saved to \(fullFile) (\(fullText.count) chars)")
