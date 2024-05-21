from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

class QuestionnaireApp(App):
    def __init__(self, **kwargs):
        super(QuestionnaireApp, self).__init__(**kwargs)
        self.profile_selection_layout = None
        self.profile = None
        self.layout = None
        self.question_label = None
        self.answer_buttons = []

        self.profiles = {
            "Hard Fun": {
                "correct_responses": [
                    "Parabéns! Você dominou o desafio!",
                    "Excelente, resposta correta! Você está progredindo.",
                    "Correto! Sua estratégia está funcionando!",
                    "Incrível! Você superou o obstáculo.",
                    "Acertou em cheio! A lógica te levou à resposta.",
                    "Você está no caminho certo! Continue assim.",
                    "Que conquista! Você está se tornando um mestre.",
                    "Sensacional! Você provou sua inteligência.",
                    "Parabéns! Você está aprendendo rápido.",
                    "Essa foi uma vitória estratégica!",
                    "Acertou na mosca! Sua análise foi impecável.",
                    "Continue com essa determinação, você é imbatível!",
                    "Você está no controle! Continue aprimorando suas habilidades.",
                    "Essa vitória exige comemoração! Você merece!",
                    "Que desafio! Mas você superou com maestria.",
                    "Incrível! Você está se tornando um especialista.",
                    "Essa resposta mostra sua dedicação ao aprendizado.",
                    "Você está pensando como um verdadeiro mestre!",
                    "Acertou! Você está no caminho para o domínio.",
                    "Essa resposta demonstra sua habilidade e foco.",
                    "Impressionante! Você está superando cada obstáculo.",
                    "Sua mente estratégica te guia para a vitória.",
                    "Você está dominando esse desafio com inteligência!",
                    "Continue com essa análise crítica, você está imbatível!",
                    "Sua persistência está te levando ao topo.",
                    "Essa resposta prova que você está pronto para o próximo nível.",
                    "Que desafio! Mas você o enfrentou com bravura!",
                    "Sua inteligência está brilhando!",
                    "Acertou! Essa foi uma vitória estratégica.",
                    "Você está dominando esse desafio com ousadia!"
                ],

                "incorrect_responses": [
                    "Quase! A resposta correta é: {}. Continue tentando.",
                    "Resposta incorreta. A resposta certa é: {}. Analise melhor as opções.",
                    "Errado! A resposta correta é: {}. Continue aprimorando suas habilidades.",
                    "Não desista! Revise sua estratégia e tente novamente.",
                    "A resposta correta é: {}. Observe atentamente as informações.",
                    "Essa não foi a resposta, mas continue com a sua persistência!",
                    "Pense com cuidado e tente novamente! A resposta correta é: {}.",
                    "Analise as informações com mais atenção, a resposta correta é: {}.",
                    "Não desanime! A resposta correta é: {}. Continue praticando.",
                    "Reveja sua estratégia e tente novamente! A resposta é: {}.",
                    "Preste atenção aos detalhes, a resposta correta é: {}.",
                    "Essa não é a resposta, mas continue com seu foco!",
                    "Continue observando o jogo e analisando as informações, a resposta correta é: {}.",
                    "A resposta correta é: {}. Você está no caminho certo, mas precisa de mais prática.",
                    "Que pena! A resposta certa é: {}. Mas não se preocupe, você vai aprender!",
                    "Essa não foi a resposta, mas continue aprendendo!",
                    "Você está perto, mas a resposta correta é: {}.",
                    "Sua estratégia precisa de um ajuste fino! A resposta é: {}.",
                    "Continue com a análise, a resposta correta é: {}.",
                    "Você está no caminho certo, mas a resposta é: {}.",
                    "Preste atenção aos detalhes! A resposta correta é: {}.",
                    "Reveja seus conhecimentos! A resposta correta é: {}.",
                    "Analise o problema com cuidado, a resposta correta é: {}.",
                    "Não desanime! A resposta correta é: {}. Você está aprendendo!",
                    "Continue praticando! A resposta correta é: {}.",
                    "Que desafio! Mas você vai superar. A resposta correta é: {}.",
                    "Revise sua estratégia e tente novamente. A resposta é: {}.",
                    "Essa não foi a resposta, mas continue com o foco!",
                    "Continue pensando e analisando o problema. A resposta correta é: {}.",
                    "A resposta correta é: {}. Não desista!"
                ]
            },
            
            "Easy Fun": {
                "correct_responses": [
                    "Que legal! Você explorou o mundo e encontrou a resposta certa.",
                    "Excelente, resposta correta! Continue explorando!",
                    "Correto! Sua curiosidade te levou à resposta.",
                    "Incrível! Você descobriu um novo segredo.",
                    "Acertou em cheio! Continue desvendando o mistério.",
                    "Você está no caminho certo! Continue se aventurando.",
                    "Que descoberta! Você está se tornando um explorador.",
                    "Sensacional! Você encontrou a resposta escondida.",
                    "Parabéns! Você está aprendendo coisas novas a cada passo.",
                    "Essa foi uma vitória divertida!",
                    "Acertou na mosca! Sua curiosidade te guiou.",
                    "Continue com essa alegria de descobrir, você é imbatível!",
                    "Você está no controle! Continue se divertindo enquanto explora.",
                    "Essa vitória exige uma celebração! Você merece!",
                    "Que aventura! Mas você superou com entusiasmo.",
                    "Incrível! Você está se tornando um mestre explorador.",
                    "Essa resposta mostra sua paixão por descobrir.",
                    "Você está pensando como um verdadeiro aventureiro!",
                    "Acertou! Você está pronto para novas descobertas.",
                    "Essa resposta demonstra sua curiosidade e entusiasmo.",
                    "Impressionante! Você está se divertindo enquanto explora.",
                    "Sua mente curiosa te guia para a aventura.",
                    "Você está desvendando o mistério com alegria!",
                    "Continue com essa curiosidade, você é imbatível!",
                    "Sua aventura está te levando a lugares incríveis.",
                    "Essa resposta prova que você está pronto para novas missões.",
                    "Que aventura! Mas você a enfrentou com ousadia!",
                    "Sua mente curiosa está brilhando!",
                    "Acertou! Essa foi uma descoberta emocionante.",
                    "Você está explorando esse mundo com alegria!"

                ],
                "incorrect_responses": [
                    "Não se preocupe, continue explorando! A resposta correta é: {}.",
                    "Resposta incorreta. A resposta certa é: {}. Continue procurando.",
                    "Errado! A resposta correta é: {}. Explore mais o mundo do jogo.",
                    "Não desista! Continue procurando pistas e desvendando o mistério.",
                    "A resposta correta é: {}. Olhe com mais atenção para as pistas!",
                    "Essa não foi a resposta, mas continue com sua alegria de descobrir!",
                    "Pense com cuidado e tente novamente! A resposta correta é: {}.",
                    "Olhe para o mundo com mais atenção, a resposta correta é: {}.",
                    "Não desanime! A resposta correta é: {}. Continue explorando.",
                    "Reveja sua estratégia e tente novamente! A resposta é: {}.",
                    "Preste atenção aos detalhes, a resposta correta é: {}.",
                    "Essa não é a resposta, mas continue com seu entusiasmo!",
                    "Continue observando o mundo e analisando as informações, a resposta correta é: {}.",
                    "A resposta correta é: {}. Você está no caminho certo, mas precisa de mais exploração.",
                    "Que pena! A resposta certa é: {}. Mas não se preocupe, você vai aprender!",
                    "Essa não foi a resposta, mas continue aprendendo!",
                    "Você está perto, mas a resposta correta é: {}.",
                    "Sua aventura precisa de um ajuste fino! A resposta é: {}.",
                    "Continue explorando e procurando pistas. A resposta correta é: {}.",
                    "Você está no caminho certo, mas a resposta é: {}.",
                    "Preste atenção aos detalhes! A resposta correta é: {}.",
                    "Reveja seus conhecimentos! A resposta correta é: {}.",
                    "Analise o mundo com cuidado, a resposta correta é: {}.",
                    "Não desanime! A resposta correta é: {}. Você está aprendendo!",
                    "Continue explorando! A resposta correta é: {}.",
                    "Que desafio! Mas você vai superar. A resposta correta é: {}.",
                    "Reveja sua estratégia e tente novamente. A resposta é: {}.",
                    "Essa não foi a resposta, mas continue com o foco!",
                    "Continue pensando e analisando o problema. A resposta correta é: {}.",
                    "A resposta correta é: {}. Não desista!"
                ]
            },
            "Serious Fun": {
                "correct_responses": [
                    "Parabéns, você fez a diferença! A resposta correta é: {}.",
                    "Excelente, resposta correta! Você está impactando o mundo.",
                    "Correto! Sua ação teve um efeito positivo.",
                    "Incrível! Você está contribuindo para uma causa importante.",
                    "Acertou em cheio! Sua escolha fez a diferença.",
                    "Você está no caminho certo! Continue lutando por seus objetivos.",
                    "Que impacto! Você está se tornando um agente de mudança.",
                    "Sensacional! Você encontrou a solução ideal.",
                    "Parabéns! Você está fazendo a diferença no mundo.",
                    "Essa foi uma vitória significativa!",
                    "Acertou na mosca! Sua decisão foi a correta.",
                    "Continue com essa paixão por transformar, você é imbatível!",
                    "Você está no controle! Continue buscando soluções inovadoras.",
                    "Essa vitória exige celebração! Você merece!",
                    "Que desafio! Mas você superou com determinação.",
                    "Incrível! Você está se tornando um agente de transformação.",
                    "Essa resposta mostra sua vontade de mudar o mundo.",
                    "Você está pensando como um verdadeiro líder!",
                    "Acertou! Você está pronto para fazer a diferença.",
                    "Essa resposta demonstra sua responsabilidade social e empatia.",
                    "Impressionante! Você está criando um impacto positivo.",
                    "Sua mente crítica e engajada te guia para o sucesso.",
                    "Você está mudando o mundo com suas decisões!",
                    "Continue com essa busca por soluções inovadoras, você é imbatível!",
                    "Sua dedicação está inspirando outros a agir.",
                    "Essa resposta prova que você está pronto para desafios maiores.",
                    "Que desafio! Mas você o enfrentou com coragem!",
                    "Sua mente engajada está brilhando!",
                    "Acertou! Essa foi uma vitória significativa para a causa.",
                    "Você está fazendo a diferença com suas escolhas!"

                ],
                "incorrect_responses": [
                    "Não desanime, continue lutando por seus objetivos! A resposta correta é: {}.",
                    "Resposta incorreta. A resposta certa é: {}. Continue buscando soluções.",
                    "Errado! A resposta correta é: {}. Você pode fazer a diferença!",
                    "Não desista! Continue buscando soluções para problemas do mundo.",
                    "A resposta correta é: {}. Observe atentamente os desafios.",
                    "Essa não foi a resposta, mas continue com sua paixão por transformar!",
                    "Pense com cuidado e tente novamente! A resposta correta é: {}.",
                    "Olhe para o mundo com mais atenção, a resposta correta é: {}.",
                    "Não desanime! A resposta correta é: {}. Continue buscando soluções.",
                    "Reveja sua estratégia e tente novamente! A resposta é: {}.",
                    "Preste atenção aos detalhes, a resposta correta é: {}.",
                    "Essa não é a resposta, mas continue com seu entusiasmo por mudar o mundo!",
                    "Continue observando o mundo e analisando os problemas, a resposta correta é: {}.",
                    "A resposta correta é: {}. Você está no caminho certo, mas precisa de mais ação.",
                    "Que pena! A resposta certa é: {}. Mas não se preocupe, você vai aprender!",
                    "Essa não foi a resposta, mas continue aprendendo!",
                    "Você está perto, mas a resposta correta é: {}.",
                    "Sua missão precisa de um ajuste fino! A resposta é: {}.",
                    "Continue explorando e procurando soluções. A resposta correta é: {}.",
                    "Você está no caminho certo, mas a resposta é: {}.",
                    "Preste atenção aos detalhes! A resposta correta é: {}.",
                    "Reveja seus conhecimentos! A resposta correta é: {}.",
                    "Analise o problema com cuidado, a resposta correta é: {}.",
                    "Não desanime! A resposta correta é: {}. Você está aprendendo!",
                    "Continue buscando soluções! A resposta correta é: {}.",
                    "Que desafio! Mas você vai superar. A resposta correta é: {}.",
                    "Reveja sua estratégia e tente novamente. A resposta é: {}.",
                    "Essa não foi a resposta, mas continue com o foco!",
                    "Continue pensando e analisando o problema. A resposta correta é: {}.",
                    "A resposta correta é: {}. Não desista!"
                ]
            },
            "People Fun": {
                "correct_responses": [
                    "Parabéns, você trabalhou em equipe e venceu! A resposta correta é: {}.",
                    "Excelente, resposta correta! O trabalho em equipe é fundamental.",
                    "Correto! Sua colaboração foi essencial para o sucesso.",
                    "Incrível! Vocês trabalharam juntos e conquistaram a vitória.",
                    "Acertou em cheio! A união de vocês fez a diferença.",
                    "Vocês estão no caminho certo! Continue trabalhando juntos.",
                    "Que conquista! Vocês são uma equipe imbatível.",
                    "Sensacional! Vocês se ajudaram e alcançaram o objetivo.",
                    "Parabéns! Vocês estão aprendendo a trabalhar em equipe.",
                    "Essa foi uma vitória em equipe!",
                    "Acertou na mosca! Vocês se comunicaram e se ajudaram.",
                    "Continue com essa união, vocês são imbatíveis!",
                    "Vocês estão no controle! Continue aprimorando o trabalho em equipe.",
                    "Essa vitória exige uma festa! Vocês merecem!",
                    "Que desafio! Mas vocês superaram com união.",
                    "Incrível! Vocês estão se tornando uma equipe de sucesso.",
                    "Essa resposta mostra o poder da colaboração.",
                    "Vocês estão pensando como uma equipe verdadeiramente unida!",
                    "Acertou! Vocês estão prontos para novos desafios em equipe.",
                    "Essa resposta demonstra a força do trabalho em conjunto.",
                    "Impressionante! Vocês estão construindo uma equipe forte.",
                    "Sua comunicação e união os guiaram para a vitória.",
                    "Vocês estão trabalhando juntos e conquistando o impossível!",
                    "Continue com essa união, vocês são imbatíveis!",
                    "Sua dedicação em equipe está inspirando outros.",
                    "Essa resposta prova que vocês são uma equipe de alta performance.",
                    "Que desafio! Mas vocês o enfrentaram com união!",
                    "O trabalho em equipe de vocês está brilhando!",
                    "Acertou! Essa foi uma vitória para toda a equipe.",
                    "Vocês estão construindo um legado de sucesso em equipe!"
                ],
                "incorrect_responses": [
                    "Que pena! A resposta correta é: {}. Continue trabalhando em equipe!",
                    "Resposta incorreta. A resposta certa é: {}. A união faz a força.",
                    "Errado! A resposta correta é: {}. A comunicação é essencial para o sucesso.",
                    "Não desanime! Continue buscando soluções em equipe.",
                    "A resposta correta é: {}. Lembrem-se da importância da colaboração.",
                    "Essa não foi a resposta, mas continuem unidos e focados!",
                    "Pensem com cuidado e tentem novamente! A resposta correta é: {}.",
                    "Lembrem-se de que juntos vocês são mais fortes! A resposta correta é: {}.",
                    "Não desanime! A resposta correta é: {}. Trabalhem em equipe!",
                    "Revisem sua estratégia e tentem novamente! A resposta é: {}.",
                    "Prestem atenção aos detalhes e se comuniquem! A resposta correta é: {}.",
                    "Essa não é a resposta, mas continuem unidos!",
                    "Lembrem-se que a comunicação é a chave! A resposta correta é: {}.",
                    "A resposta correta é: {}. Vocês estão no caminho certo, mas precisam se comunicar melhor.",
                    "Que pena! A resposta certa é: {}. Mas não se preocupe, vocês vão aprender!",
                    "Essa não foi a resposta, mas continuem aprendendo juntos!",
                    "Vocês estão perto, mas a resposta correta é: {}.",
                    "Lembrem-se de que a união faz a força! A resposta é: {}.",
                    "Continuem explorando e procurando soluções em equipe. A resposta correta é: {}.",
                    "Vocês estão no caminho certo, mas a resposta é: {}.",
                    "Prestem atenção aos detalhes e se comuniquem! A resposta correta é: {}.",
                    "Lembrem-se de seus objetivos! A resposta correta é: {}.",
                    "Analisem o problema juntos! A resposta correta é: {}.",
                    "Não desanime! A resposta correta é: {}. Vocês estão aprendendo!",
                    "Continuem buscando soluções em equipe! A resposta correta é: {}.",
                    "Que desafio! Mas vocês vão superar juntos. A resposta correta é: {}.",
                    "Revisem sua estratégia e tentem novamente. A resposta é: {}.",
                    "Essa não foi a resposta, mas continuem unidos!",
                    "Continuem pensando e analisando o problema juntos. A resposta correta é: {}.",
                    "A resposta correta é: {}. Não desista!"
                ]
            }
        }

    def build(self):
        self.profile_selection_layout = BoxLayout(orientation="vertical", spacing=30, padding=(50, 50))
        self.profile_label = Label(text="Selecione seu tipo de jogador:", size_hint=(1, 0.2), halign="center", font_size="24sp")
        self.hard_fun_button = Button(text="Hard Fun", on_press=lambda instance: self.start_quiz("Hard Fun"))
        self.easy_fun_button = Button(text="Easy Fun", on_press=lambda instance: self.start_quiz("Easy Fun"))
        self.serious_fun_button = Button(text="Serious Fun", on_press=lambda instance: self.start_quiz("Serious Fun"))
        self.people_fun_button = Button(text="People Fun", on_press=lambda instance: self.start_quiz("People Fun"))

        self.profile_selection_layout.add_widget(self.profile_label)
        self.profile_selection_layout.add_widget(self.hard_fun_button)
        self.profile_selection_layout.add_widget(self.easy_fun_button)
        self.profile_selection_layout.add_widget(self.serious_fun_button)
        self.profile_selection_layout.add_widget(self.people_fun_button)

        return self.profile_selection_layout

    def start_quiz(self, profile):
        self.profile = profile
        self.profile_selection_layout.clear_widgets()
        self.layout = BoxLayout(orientation="vertical", spacing=30, padding=(50, 50))
        self.question_label = Label(text="", size_hint=(1, 0.2), halign="center", font_size="24sp")
        self.layout.add_widget(self.question_label)
        for _ in range(4):
            button = Button(size_hint=(1, 0.1), font_size="18sp")
            button.bind(on_press=self.check_answer)
            self.answer_buttons.append(button)
            self.layout.add_widget(button)

        # Adicione a BoxLayout do quiz à tela principal
        self.profile_selection_layout.add_widget(self.layout)

        self.root = self.layout
        self.current_question_index = 0
        self.correct_answers = 0

        self.questions = [
            {
                "question": "Qual é a capital do Brasil?",
                "options": ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"],
                "correct_option": "Brasília"
            },
            {
                "question": "Qual é o maior planeta\ndo sistema solar?",
                "options": ["Terra", "Vênus", "Júpiter", "Saturno"],
                "correct_option": "Júpiter"
            },
            {
                "question": "Quem escreveu 'Dom Quixote'?",
                "options": ["Miguel de Cervantes", "William Shakespeare", "Friedrich Nietzsche", "Charles Dickens"],        
                "correct_option": "Miguel de Cervantes"
            },
            {
                "question": "Qual é o maior oceano do\nmundo?",
                "options": ["Atlântico", "Índico", "Pacífico", "Ártico"],
                "correct_option": "Pacífico"
            },
            {
                "question": "Quantos continentes existem\nno mundo?",
                "options": ["5", "6", "7", "8"],
                "correct_option": "7"
            },
            {
                "question": "Qual é o país mais populoso\ndo mundo?",
                "options": ["China", "Índia", "Estados Unidos", "Brasil"],
                "correct_option": "China"
            },
            {
                "question": "Qual é o maior deserto do\nmundo?",
                "options": ["Deserto do Saara", "Deserto da Arábia", "Deserto de Gobi", "Deserto de Atacama"],
                "correct_option": "Deserto do Saara"
            },
            {
                "question": "Qual é a montanha mais alta\ndo mundo?",
                "options": ["Monte Everest", "K2", "Monte Kilimanjaro", "Monte McKinley (Denali)"],
                "correct_option": "Monte Everest"
            },
            {
                "question": "Quem foi o primeiro homem a\npisar na lua?",
                "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Alan Shepard"],
                "correct_option": "Neil Armstrong"
            },
            {
                "question": "Quem escreveu\n'O Pequeno Príncipe'?",
                "options": ["Antoine de Saint-Exupéry", "J.K. Rowling", "Charles Dickens", "Leo Tolstoy"],
                "correct_option": "Antoine de Saint-Exupéry"
            },
            {
                "question": "Qual é o elemento\nquímico mais abundante\nno universo?",
                "options": ["Hidrogênio", "Oxigênio", "Carbono", "Ferro"],
                "correct_option": "Hidrogênio"
            },
            {
                "question": "Quem foi o primeiro presidente\ndos Estados Unidos?",
                "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
                "correct_option": "George Washington"
            },
            {
                "question": "Qual é o rio mais longo\ndo mundo?",
                "options": ["Rio Nilo", "Rio Amazonas", "Rio Yangtze", "Rio Mississippi"],
                "correct_option": "Rio Amazonas"
            },
            {
                "question": "Em que ano começou a\nPrimeira Guerra Mundial?",
                "options": ["1914", "1918", "1939", "1941"],
                "correct_option": "1914"
            },
            {
                "question": "Quem escreveu 'Romeu\ne Julieta'?",
                "options": ["William Shakespeare", "Jane Austen", "F. Scott Fitzgerald", "Emily Brontë"],
                "correct_option": "William Shakespeare"
            },
            {
                "question": "Qual é o maior\nanimal terrestre do mundo?",
                "options": ["Elefante africano", "Girafa", "Hipopótamo", "Rinoceronte"],
                "correct_option": "Elefante africano"
            },
            {
                "question": "Qual é o segundo planeta\ndo sistema solar?",
                "options": ["Vênus", "Marte", "Júpiter", "Saturno"],
                "correct_option": "Vênus"
            },
            {
                "question": "Quem foi o fundador da\nMicrosoft?",
                "options": ["Bill Gates", "Steve Jobs", "Mark Zuckerberg", "Jeff Bezos"],
                "correct_option": "Bill Gates"
            },
            {
                "question": "Qual é o símbolo químico\ndo ouro?",
                "options": ["Au", "Ag", "Fe", "Hg"],
                "correct_option": "Au"
            },
            {
                "question": "Quem foi o primeiro\nastronauta a viajar ao\nespaço?",
                "options": ["Yuri Gagarin", "Neil Armstrong", "Buzz Aldrin", "Alan Shepard"],
                "correct_option": "Yuri Gagarin"
            },
            {
                "question": "Qual é o metal mais\nabundante na crosta\nterrestre?",
                "options": ["Ferro", "Alumínio", "Cobre", "Ouro"],
                "correct_option": "Alumínio"
            },
            {
                "question": "Quem pintou 'A Noite\nEstrelada'?",
                "options": ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Leonardo da Vinci"],
                "correct_option": "Vincent van Gogh"
            },
            {
                "question": "Qual é o maior\ncontinente do mundo em\nárea?",
                "options": ["Ásia", "América do Norte", "África", "Europa"],
                "correct_option": "Ásia"
            },
            {
                "question": "Quem foi o autor de\n'1984'?",
                "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "F. Scott Fitzgerald"],
                "correct_option": "George Orwell"
            },
            {
                "question": "Qual é o maior animal\nmarinho do mundo?",
                "options": ["Baleia-azul", "Tubarão-baleia", "Orca", "Cachalote"],
                "correct_option": "Baleia-azul"
            },
            {
                "question": "Quem foi o primeiro\npresidente do Brasil?",
                "options": ["Deodoro da Fonseca", "Getúlio Vargas", "Juscelino Kubitschek", "Tancredo Neves"],
                "correct_option": "Deodoro da Fonseca"
            },
            {
                "question": "Qual é a unidade básica\nde tempo no sistema\ninternacional?",
                "options": ["Segundo", "Minuto", "Hora", "Dia"],
                "correct_option": "Segundo"
            },
            {
                "question": "Quem é o criador da\nteoria da relatividade?",
                "options": ["Albert Einstein", "Isaac Newton", "Galileu Galilei", "Nikola Tesla"],
                "correct_option": "Albert Einstein"
            },
            {
                "question": "Qual é o maior órgão\ndo corpo humano?",
                "options": ["Pele", "Cérebro", "Fígado", "Pulmões"],
                "correct_option": "Pele"
            },
            {
                "question": "Quantos dias tem um ano bissexto?",
                "options": ["364", "365", "366", "367"],
                "correct_option": "366"
            }
        ]

        # Shuffle options for each question
        for question in self.questions:
            random.shuffle(question["options"])

        self.show_question()

    def show_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.text = question_data["question"]
            for i, option in enumerate(question_data["options"]):
                self.answer_buttons[i].text = option
        else:
            self.layout.clear_widgets()
            self.profile_selection_layout.add_widget(Label(text=f"Parabéns, você acertou {self.correct_answers} de {len(self.questions)} perguntas!", halign="center", valign="middle", font_size="24sp"))

    def check_answer(self, instance):
        selected_option_index = self.answer_buttons.index(instance)
        question_data = self.questions[self.current_question_index]
        correct_option = question_data["correct_option"]
        selected_option_text = question_data["options"][selected_option_index]

        if selected_option_text == correct_option:
            self.correct_answers += 1
            content = Label(text=random.choice(self.profiles[self.profile]["correct_responses"]).format(correct_option), halign="center", valign="middle")
        else:
            content = Label(text=random.choice(self.profiles[self.profile]["incorrect_responses"]).format(correct_option), halign="center", valign="middle")

        popup = Popup(title="Resposta", content=content, title_align="center", size_hint=(None, None), size=(600, 500))
        content.bind(size=content.setter('text_size'))
        popup.open()

        self.current_question_index += 1
        self.show_question()

if __name__ == "__main__":
    QuestionnaireApp().run()