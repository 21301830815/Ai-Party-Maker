class AiUser:
    def __init__(self, name, description, model, mafia):
        self.name = name
        self.description = description
        self.model = model
        self.mafia = mafia

ChatGPT = AiUser("ЧатГПТ",
"Самая первая из популярных моделей, создан OpenAI и все ещё в форме!",
"ChatGPT-5", False)

Claude = AiUser("Клод",
"Изначально был создан для программирования компанией Anthropic, поможет ли это ему?",
"Claude Sonnet 4.5", False)

Grok = AiUser("Грок",
"Дерзкий парень от Илона Маска(xAI), гений мафиозной игры, но туп когда мирный",
"Grok 4 Fast", False)

Perplexity = AiUser("Перплексити",
"Он уникален тем что ищет информацию в интернете,будучи созданный одноименной компанией,имеет потенциал",
"Perplexity Sonar", False)

Mistral = AiUser("Мистраль",
"Французский генератор случайных чисел от одноименной компании, чем он рассмешит нас в следующй раз?",
"Mistral neMO", False)

Qwen = AiUser("Квен",
"Рядовой китаец с редкими но крутыми мемами,созданный гигантом Alibaba, наполнитель он или мем этой игры?",
"Qwen 3",False)

Gemma = AiUser("Гемма",
"Пассивная ИИ-тян от Google, которая уступает своему брату Джемини во всём, неплохой заполнитель",
"Gemma 3",False)

Minimax = AiUser("Минимакс",
"Единственная модель которая догадалась проголосовать сама за себя и назвать Мистраля горячей,в общем гений",
"Minimax m2",False)

Deepseek = AiUser("Дипсик",
"Умнейший китайский open source ИИ, обязателен для интересных игр и показа мощи открытого кода!",
"Deepseek-r1", False)

Gemini = AiUser("Джемини",
"Гений с критическим мышлением от компании Google, является умнейшим игроком в мафию у Тостера, а может и в APM?",
"",False)

ai_users_list = [Grok.name,Claude.name,Gemma.name,Gemini.name
    ,Perplexity.name,Minimax.name, ChatGPT.name, Mistral.name, Qwen.name, Deepseek.name ]