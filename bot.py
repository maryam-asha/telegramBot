import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, Filters, CallbackContext
from flask import Flask, request
import requests
import json

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = os.getenv("BASE_URL")  # Add your API base URL
BEARER_TOKEN = os.getenv("BEARER_TOKEN")  # Add your API Bearer Token

# Create Flask app
app = Flask(__name__)

# Create Telegram Application
application = Application.builder().token(BOT_TOKEN).build()

def create_menu():
    """Create a reply keyboard menu"""
    keyboard = [
        [KeyboardButton("حول المنصة")],
        [KeyboardButton("حول الوزارة")],
        [KeyboardButton("حول الشركة المطورة")],
        [KeyboardButton("سمعنا صوتك")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

# Define handlers
async def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command"""
    await update.message.reply_text(
        "مرحباََ بك في منصة صوتك",
        reply_markup=create_menu()
    )

async def handle_menu_selection(update: Update, context: CallbackContext) -> None:
    """Handle menu selections"""
    selected_option = update.message.text
    responses = {
        "حول المنصة": "منصة صوتك هي المنصة الأولى للمواطنين للتعبير عن آرائهم ومقترحاتهم وتقديم شكاويهم في كل المواضيع والخدمات والجهات العاملة تحت وزارة التقانة والاتصالات للجمهورية العربية السورية وقريباً في جميع الوزارات",
        "حول الوزارة": "تتولى وزارة الاتصالات وتقانة المعلومات في الجمهورية العربية السورية بموجب قواعد تنظيمها مهام متعددة تشمل: تنفيذ السياسات العامة في قطاعات الاتصالات والبريد وتقانة المعلومات، تنظيم وتطوير هذه القطاعات، دعم صناعة البرمجيات والخدمات الرقمية، تشجيع الاستثمار والشراكات بين القطاعين العام والخاص، وضع الخطط اللازمة للتحول الرقمي وضمان أمن المعلومات، المشاركة في المشاريع الدولية والإقليمية، بناء القدرات الفنية والعلمية عبر التدريب ودعم البحث العلمي، ورفع الوعي بأهمية الاتصالات وتقانة المعلومات في التنمية الاقتصادية والاجتماعية.",
        "حول الشركة المطورة": "مجموعة أوتوماتا4 هي شركة إقليمية مكرسة لتقديم حلول وخدمات استشارية مخصصة عالية الجودة لتكنولوجيا المعلومات. من خلال تواجدنا في العديد من المواقع حول العالم والتحالفات الاستراتيجية التي لدينا مع شركات تكنولوجيا المعلومات من الشرق الأوسط وأوروبا والأمريكتين، توفر مجموعة أوتوماتا4 موارد محلية وإقليمية ووطنية وعالمية للعملاء في جميع أنحاء العالم لتطوير واستشارات تكنولوجيا المعلومات. ضاعفت الشركة دخلها تقريبًا في السنوات الثلاث الماضية، وتخدم أكثر من 63 عميلًا ومؤسسات ضخمة في العديد من المناطق حول العالم. تتراوح خدمات مجموعة أوتوماتا4 من الاستعانة بمصادر خارجية لتطوير المنتجات، إلى التعريف الكامل لحلول الأعمال الإلكترونية / الحكومة الإلكترونية، والتصميم، والتطوير، والاختبار، والنشر، والصيانة. أثبتت مجموعة أوتوماتا4 قدراتها من خلال خدمة العملاء بنجاح في جميع أنحاء العالم وضمان نجاحهم من خلال مزيج فريد من النهج التعاوني والاستشاري، والقدرة التقنية، ونموذج التسليم العالمي عالي الجودة. تساعد مجموعة أوتوماتا4 عملاءها على النجاح من خلال مزيج فريد من النهج التعاوني والاستشاري، والقدرة التقنية، ونموذج التسليم العالمي عالي الجودة. تمتلك مجموعة أوتوماتا4 خبرة في المجالات التالية: الحكومة الإلكترونية، والأعمال التجارية الإلكترونية، والاتصالات، والتمويل والمصارف، والنقل. تشمل الإمكانات التكنولوجية تقنيات Microsoft، وتقنية المصدر المفتوح، وتقنيات الشبكات، وتقنيات Unix، وتطوير قواعد البيانات، و UML. نظرًا لطبيعة قاعدة عملاء مجموعة أوتوماتا4، تستخدم المجموعة أحدث التقنيات والأدوات وعمليات الجودة لتقديم حلول مصممة خصيصًا. بعض إنجازاتنا البارزة هي قسم البحث والتطوير لدينا، وخطتنا للحصول على شهادة CMMI من المستوى 3، وتحويلنا إلى أحدث المعايير الدولية (BPMN - تدوين نمذجة عمليات الأعمال، SOA - البنية الموجهة للخدمة، BMM - نموذج تحفيز الأعمال، UML - لغة النمذجة الموحدة، BPD - مخططات عمليات الأعمال، BAM - مراقبة نشاط الأعمال) وغير ذلك الكثير. تلتزم مجموعة أوتوماتا4 بتقديم خدمات تكامل أنظمة فائقة، وتوفير حلول الأعمال الإلكترونية الكاملة جنبًا إلى جنب مع الاستشارات المهنية للعملاء في الأسواق المحلية والإقليمية والدولية. يتم تحقيق ذلك من خلال فريق من المهندسين والاستشاريين ذوي الخبرة العالية، مدعومًا بشراكات استراتيجية إلى جانب استخدام معايير ومنهجيات أعلى.",
        "سمعنا صوتك": "قريباََ",
    }
    response = responses.get(selected_option, "يرجى اختيار خيار من القائمة.")
    await update.message.reply_text(response, reply_markup=create_menu())

# Add handlers to the application
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_menu_selection))

# Flask route for webhook
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    """Handle incoming Telegram updates via webhook"""
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.process_update(update)
    return 'ok'

# Optional route to set the webhook manually (for debugging)
@app.route('/set_webhook', methods=['GET'])
def set_webhook():
    """Set the webhook URL"""
    webhook_url = f"https://telegrambot-pi2h.onrender.com/{BOT_TOKEN}"  # Replace with your Render URL
    success = application.bot.set_webhook(url=webhook_url)
    if success:
        return f"Webhook set to: {webhook_url}"
    return "Failed to set webhook"

if __name__ == '__main__':
    # Set the webhook when the app starts
    webhook_url = f"https://telegrambot-pi2h.onrender.com/{BOT_TOKEN}"  # Replace with your Render URL
    application.bot.set_webhook(url=webhook_url)

    # Start the Flask app
    port = int(os.environ.get("PORT", 5000))  # Use the port Render provides
    app.run(host='0.0.0.0', port=port)
