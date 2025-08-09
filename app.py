from flask import Flask, request, jsonify

app = Flask(__name__)

# مسار فحص السيرفر
@app.get("/health")
def health():
    return {"status": "ok"}

# مسار توليد القالب (نسخة تجريبية)
@app.post("/api/generate")
def generate():
    data = request.get_json(force=True) if request.data else {}
    topic = data.get("topic", "Newsletter")
    tone = data.get("tone", "friendly")
    cta  = data.get("cta", "Shop Now")

    # HTML تجريبي - لاحقاً سنربطه بـ OpenAI API
    html = f"""
    <!doctype html>
    <html dir="rtl" lang="ar">
    <head><meta charset="utf-8"><title>{topic}</title></head>
    <body style="font-family:Arial,sans-serif">
      <h1>{topic}</h1>
      <p>نبرة الكتابة: {tone}</p>
      <a href="#" style="display:inline-block;padding:12px 20px;border-radius:6px;background:#111;color:#fff;text-decoration:none">{cta}</a>
    </body>
    </html>
    """

    return jsonify({
        "title": topic,
        "preheader": "هذا مجرد إخراج تجريبي",
        "html": html
    })

if __name__ == "__main__":
    # تشغيل محلياً على المنفذ 5000
    app.run(host="127.0.0.1", port=5000, debug=True)
