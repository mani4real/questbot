import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telepot.loop import MessageLoop
import time
biologyText = "زیست شناسی 🧬"
mathText = "ریاضی 🔢"
physicsText = "فیزیک 🌌"
chemistryText = "شیمی 🧪"
theoText = "دینی 📿"
farsiText = "فارسی 📖"
arabicText = "عربی 👳‍♂️"
engText = " زبان انگلیسی🔤"
geometryText = "هندسه 📐"
qaVars = {'physics':'فیزیک', 'math':'ریاضی', 'biology':'زیست شناسی', 'chem':'شیمی', 'theo':"دینی",
            'farsi' : 'فارسی', 'geometry':'هندسه', 'eng':'زبان انگلیسی', 'arabic':"عربی"}
startText = """سلام ...👋😃
به ربات سوال و جواب خوش اومدی🤓
اینجا میتونی اشکالای درسی خودتو بپرسی📕
برای اینکار کافیه این دستور رو تایپ کنی:⌨️
/question
یا اینکه سوالای بقیه رو جواب بدی📝‏
برای اینکار کافیه این دستور رو تایپ کنی:⌨️
/answer"""
questionText = """خب خب خب ظاهرا میخوای اشکال بپرسی☺️
لطفاً مبحثی که توش مشکل داری رو انتخاب کن☑️"""
answerDisconfirmationText = "مشکلی نیست، پس یه بار دیگه جوابو برامون بفرست🤗"
questiondDisconfirmationText = """خب طوری نیست🤗
پس سوالتو اصلاح کن و همینجا برام بفرست😃"""
questionAnsweredText = """خب ظاهرا یکی این سوالتو جواب داد😊
الان جوابشو برات میفرستم☺️"""
noQuestionsAfterThis = """سوال دیگه ای بعد از این توی این مبحث پرسیده نشده🧐
اگه میدونی سوال دیگه ای وجود داره، دو حالت داره🤓
یا از آینده اومدی، که خب، خیلی خفنی😲
یا مشکل از سرور ماست، عذرخواهی میکنیم🥺"""
questionConfirmText = "خب همین سوالو میخوای به اشتراک بذاری؟"
answerConfirmedText = """جوابت ارسال شد🥳
خیلی ممنونیم از اینکه برای جواب دادن به این سوال وقت گذاشتی🌹"""
questionSolved = """بسیار عالی🤗
خوشحالیم که تونستیم توی حل اشکال کمکت کنیم😍"""
sendMeQuestionText = """آهان☺️
فکر کنم توی مبحث TOPIC اشکال داری📝
برامون اشکالتو به صورت یه متن بفرست🤗"""
noQuestionsToAnswerText = """عه🤨
ای بابا، ظاهرا سوال جدیدی از این مبحث نداریم...😞
ولی طوری نیست 😉
میتونی یه مبحث دیگه رو انتخاب کنی☑️
یا اینکه بعدا بیای و سوالامونو چک کنی⏱"""
answerCallback = """خوبه، میخوای سوالای TOPIC رو جواب بدی😌
خب سوالا رو برات میفرستیم هر کدوم رو تونستی لطفا جواب بده📝🤓"""
sendMeAnswerText = """بسیار خب😀
میخوای این سوال رو جواب بدی🤓
جوابتو به صورت یه متن برامون بفرست📝
سعی کن کاملترین جواب رو بهمون بدی🙂
ممنون🌹"""
contactText = """برای ارسال انتقادات، پیشنهادات یا هر چیز دیگه به سازنده این ربات، میتونین از طریق آیدی:
@eternalguy
باهاش در ارتباط باشین🤗"""
thankYouAnswer = """راستی
خیلی ممنونیم ازت که این سوال رو جواب دادی🤗🌹
همین الان بهمون گفتن که جوابت درست بوده و کسی که این سوالو پرسیده جوابتو فهمیده🥳"""
answerConfirmText = """مطمئنی این جواب رو میخوای بفرستی؟"""
answerText = """خب ایول🙂
پس میخوای سوال بقیه رو جواب بدی🤓
موضوعی که توش تسلط داری رو بهمون بگو📝"""
questiondSubmittedText = """بسیار خب 😊
سوالت ثبت شد🥳
به محض اینکه یه نفر جوابش بده، جوابو برات میفرستیم🤓"""
noQuestionsBeforeThis="""و قبل از پرسیده شدن این سوال، دایناسورها بر روی زمین زندگی میکردند...🦖
سوالی قبل از این توی این مبحث وجود نداره😁"""
token = "1252393429:AAFbFATFdTxKoMYOb8BzRbwWQ6bUPdenneg"
Bot = telepot.Bot(token)
unsolvedQuestions = {'physics':[], 'math':[], 'biology':[], 'chem':[], 'theo':[],
            'farsi' : [], 'geometry':[], 'eng':[], 'arabic':[]}
print(Bot.getMe())
openAnswer = {}
confirmAsk = {}
answerIndex = {}
answerTopic={}
confirmAnswer = {}
openAsk = {}
def loop(msg):
    global openAnswer
    global openAsk
    try:
        content_type, chat_type, chat_id = telepot.glance(msg)
    except Exception:
        content_type = "instanceData"
        chat_type = msg['message']['chat']['type']
        chat_id = msg['message']['chat']['id']
    #print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if msg['text'] == '/start':
            Bot.sendMessage(chat_id, startText.replace('...',msg['from']['first_name']))
        if msg['text'] == '/contact':
            Bot.sendMessage(chat_id, contactText)
        elif msg['text'] == '/question':
            if chat_id in openAsk:
                openAsk.__delitem__(chat_id)
            if chat_id in openAnswer:
                openAnswer.__delitem__(chat_id)
            Bot.sendMessage(chat_id, questionText,reply_markup = InlineKeyboardMarkup(inline_keyboard=[
                                    [InlineKeyboardButton(text=biologyText,callback_data="qbiology"), InlineKeyboardButton(text = mathText,callback_data='qmath'), InlineKeyboardButton(text = physicsText, callback_data='qphysics')],
                                    [InlineKeyboardButton(text=chemistryText,callback_data='qchem'), InlineKeyboardButton(text = theoText, callback_data='qtheo'), InlineKeyboardButton(text = farsiText, callback_data = 'qfarsi')],
                                    [InlineKeyboardButton(text=arabicText, callback_data = "qarabic"), InlineKeyboardButton(text = engText, callback_data="qeng"), InlineKeyboardButton(text = geometryText, callback_data="qgeometry")]
                                ]
                            ))
        elif msg['text'] == '/answer':
            if chat_id in openAsk:
                openAsk.__delitem__(chat_id)
            if chat_id in openAnswer:
                openAnswer.__delitem__(chat_id)
            Bot.sendMessage(chat_id, answerText,reply_markup = InlineKeyboardMarkup(inline_keyboard=[
                                    [InlineKeyboardButton(text=biologyText,callback_data="xbiology"), InlineKeyboardButton(text = mathText,callback_data='xmath'), InlineKeyboardButton(text = physicsText, callback_data='xphysics')],
                                    [InlineKeyboardButton(text=chemistryText,callback_data='xchem'), InlineKeyboardButton(text = theoText, callback_data='xtheo'), InlineKeyboardButton(text = farsiText, callback_data = 'xfarsi')],
                                    [InlineKeyboardButton(text=arabicText, callback_data = "xarabic"), InlineKeyboardButton(text = engText, callback_data="xeng"), InlineKeyboardButton(text = geometryText, callback_data="xgeometry")]
                                ]
                            ))
        elif msg['text'] == '/test':
            pass
        elif chat_id in openAsk:
            question = '&`and;&' + str(msg['message_id']) + '&`and;&' + str(msg['chat']['id'])
            Bot.sendMessage(chat_id, questionConfirmText, reply_markup = InlineKeyboardMarkup(inline_keyboard=
                                [[InlineKeyboardButton(text = "بله", callback_data="confirmAskYes" + question),InlineKeyboardButton(text = "خیر", callback_data="confirmAskNo")]]))
            confirmAsk[chat_id] = str(msg['text'])
        elif chat_id in openAnswer:
            Bot.sendMessage(chat_id, answerConfirmText, reply_markup = InlineKeyboardMarkup(inline_keyboard=
                                [[InlineKeyboardButton(text = "بله", callback_data="confirmAnswerYes"),InlineKeyboardButton(text = "خیر", callback_data="confirmAnswerNo")]]))
            confirmAnswer[chat_id] = str(msg['text']) 
    elif content_type == 'image':
        if chat_id in openAsk:
            #Bot.se
            pass
    elif content_type == "instanceData": 
        
        currData = str(msg['data'])
        if(currData[0] == 'q'):
            currData = currData.replace('q','')
            Bot.sendMessage(chat_id, sendMeQuestionText.replace('TOPIC',qaVars[currData]))
            openAsk[chat_id] = currData
        elif(currData[0] == 'x'):
            currData = currData.replace('x','')
            thisTopic = answerCallback.replace('TOPIC',qaVars[currData])
            Bot.sendMessage(chat_id, thisTopic, reply_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="بفرست!", callback_data="startAnswering")]]))
            answerIndex[chat_id] = 0
            answerTopic[chat_id] = currData
        elif("confirmAskYes&`and;&" in currData) and chat_id in openAsk and chat_id in confirmAsk:
            extracted = currData.split('&`and;&')[1:3]
            extracted.append(confirmAsk[chat_id])
            unsolvedQuestions[openAsk[chat_id]].append(extracted)
            confirmAsk.__delitem__(chat_id)
            Bot.sendMessage(chat_id,questiondSubmittedText)
            openAsk.__delitem__(chat_id)
        elif currData == 'confirmAskNo' and chat_id in openAsk and chat_id in confirmAsk:
            Bot.sendMessage(chat_id, questiondDisconfirmationText)
        elif currData == 'confirmAnswerYes' and chat_id in openAnswer and chat_id in confirmAnswer:
            questionID, senderID, question = openAnswer[chat_id]
            qTopic = answerTopic[chat_id]
            Bot.sendMessage(chat_id, answerConfirmedText)
            answeredNow = """خب ظاهرا یکی سوالتو جواب داد😊
الان جوابشو برات میفرستم☺️"""
            CBdata = "#ok&"+qTopic+'&'+str(questionID)+'&'+str(chat_id)
            sendITANS = question + '\n\n' + answeredNow
            Bot.sendMessage(int(senderID), sendITANS)
            Bot.sendMessage(int(senderID), confirmAnswer[chat_id], reply_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="این جواب درسته و من فهمیدمش", callback_data=CBdata)]]))
            openAnswer.__delitem__(chat_id)
            answerTopic.__delitem__(chat_id)
            answerIndex.__delitem__(chat_id)
            confirmAnswer.__delitem__(chat_id)
        elif '#ok' in currData:
            ok, topic, qID, answerID = currData.split('&')
            for quest in unsolvedQuestions[topic]:
                if quest[0] == qID:
                    sendThanks = quest[2] + '\n\n' + thankYouAnswer
                    Bot.sendMessage(int(answerID),sendThanks)
                    unsolvedQuestions[topic].remove(quest)
                    Bot.sendMessage(chat_id, questionSolved)
                    break
        elif currData == 'confirmAnswerNo' and chat_id in openAnswer and chat_id in confirmAnswer:
            Bot.sendMessage(chat_id, answerDisconfirmationText)
        elif "answerThisOne" in currData:
            thisIndex = int(currData.replace("answerThisOne",""))
            openAnswer[chat_id] = unsolvedQuestions[answerTopic[chat_id]][thisIndex]
            Bot.sendMessage(chat_id, sendMeAnswerText)
        elif "startAnswering" in currData:
            if(len(unsolvedQuestions[answerTopic[chat_id]]) == 0):
                Bot.sendMessage(chat_id, noQuestionsToAnswerText)
            elif "&prev" in currData:
                if(answerIndex[chat_id]>0):
                    answerIndex[chat_id]-=1
                    currIndex = str(answerIndex[chat_id])
                    Bot.sendMessage(chat_id, unsolvedQuestions[answerTopic[chat_id]][answerIndex[chat_id]][2], reply_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="بعدی", callback_data="startAnswering&next"),InlineKeyboardButton(text="قبلی", callback_data="startAnswering&prev")],[InlineKeyboardButton(text="همینو جواب میدم!", callback_data="answerThisOne"+currIndex)]]))
                else:
                    Bot.sendMessage(chat_id,noQuestionsBeforeThis)
            elif "&next" in currData:
                if(answerIndex[chat_id]<len(unsolvedQuestions[answerTopic[chat_id]])-1):
                    answerIndex[chat_id]+=1
                    currIndex = str(answerIndex[chat_id])
                    Bot.sendMessage(chat_id, unsolvedQuestions[answerTopic[chat_id]][answerIndex[chat_id]][2], reply_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="بعدی", callback_data="startAnswering&next"),InlineKeyboardButton(text="قبلی", callback_data="startAnswering&prev")],[InlineKeyboardButton(text="همینو جواب میدم!", callback_data="answerThisOne"+currIndex)]]))
                else:
                    Bot.sendMessage(chat_id,noQuestionsAfterThis)
            else:
                currIndex = str(answerIndex[chat_id])
                Bot.sendMessage(chat_id, unsolvedQuestions[answerTopic[chat_id]][answerIndex[chat_id]][2], reply_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="بعدی", callback_data="startAnswering&next"),InlineKeyboardButton(text="قبلی", callback_data="startAnswering&prev")],[InlineKeyboardButton(text="همینو جواب میدم!", callback_data="answerThisOne"+currIndex)]]))
MessageLoop(Bot, loop).run_as_thread()
while 1:
    time.sleep(10)