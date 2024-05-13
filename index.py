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
            "Rígido": 
            {
                "correct_responses": [
                    "Correto. Mas não se acomode, o próximo desafio será maior.",
                    "Resposta precisa. Continue se esforçando para manter esse nível.",
                    "Acertou. Conhecimento é poder, use-o com sabedoria.",
                    "Exato. Mas não se iluda, a jornada rumo à excelência é longa.",
                    "Correto. Continue aprimorando suas habilidades, a jornada apenas começou.",
                    "Resposta impecável. Mas lembre-se, a perfeição exige dedicação constante.",
                    "Acertou em cheio. No entanto, o verdadeiro teste ainda está por vir.",
                    "Exato. Continue buscando conhecimento, a ignorância é a inimiga do sucesso.",
                    "Resposta precisa. A disciplina é a chave para alcançar seus objetivos.",
                    "Correto. Mas não se distraia, o foco é essencial para o sucesso.",
                    "Ótimo trabalho! Mas não se esqueça, a arrogância precede a queda.",
                    "Resposta correta. Continue aprimorando seus métodos, a otimização é crucial.",
                    "Acertou. A busca pelo conhecimento é um caminho sem fim, nunca pare de aprender.",
                    "Exato. A perseverança é fundamental para superar os obstáculos.",
                    "Correto. Mas não se contente com pouco, mire sempre no topo.",
                    "Resposta impecável. A inteligência é um dom, use-o com responsabilidade.",
                    "Acertou em cheio. Mas lembre-se, o sucesso é construído passo a passo.",
                    "Exato. Continue investindo em seu conhecimento, ele é seu maior patrimônio.",
                    "Resposta precisa. A precisão é essencial para alcançar resultados eficazes.",
                    "Correto. Mas não se acomode em sua zona de conforto, o crescimento exige desafios.",
                    "Ótimo trabalho! Mas mantenha os pés no chão, a humildade é essencial.",
                    "Resposta correta. A análise crítica é fundamental para o aprendizado.",
                    "Acertou. Continue explorando novas ideias, a inovação é a chave para o progresso.",
                    "Exato. A persistência é a diferença entre o sucesso e o fracasso.",
                    "Correto. Mas não se distraia com o sucesso, o foco deve ser mantido."
                    "Resposta impecável. O conhecimento é a base para a tomada de decisões inteligentes.",
                    "Acertou em cheio. Mas lembre-se, o aprendizado é um processo contínuo.",
                    "Exato. Continue se desafiando, a superação é o motor da evolução.",
                    "Resposta precisa. O domínio do conhecimento requer prática e dedicação.",
                    "Correto. Mas não se iluda, a jornada rumo ao topo é árdua e exige sacrifícios."

                ],
                "incorrect_responses": [
                    "Estude mais, a resposta correta é: {}.",
                    "A resposta está errada. Dedique-se mais aos estudos, a resposta correta é: {}.",
                    "Sua resposta demonstra falta de atenção. A resposta correta é: {}.",
                    "É preciso se esforçar mais para alcançar o sucesso. A resposta correta é: {}.",
                    "O caminho para o conhecimento exige disciplina e foco. A resposta correta é: {}.",
                    "A resposta incorreta indica a necessidade de revisão do conteúdo. A resposta correta é: {}.",
                    "O erro é parte do processo, mas a persistência é fundamental. A resposta correta é: {}.",
                    "Analise seus erros e busque aprimoramento. A resposta correta é: {}.",
                    "A resposta incorreta evidencia a importância da atenção aos detalhes. A resposta correta é: {}.",
                    "O sucesso exige dedicação e esforço contínuos. A resposta correta é: {}.",
                    "Não desanime com o erro, utilize-o como aprendizado. A resposta correta é: {}.",
                    "A resposta incorreta aponta para a necessidade de aprimorar seus métodos de estudo. A resposta correta é: {}.",
                    "A busca pela excelência exige constante aprimoramento. A resposta correta é: {}.",
                    "O erro é uma oportunidade para identificar suas fraquezas e superá-las. A resposta correta é: {}.",
                    "A resposta incorreta ressalta a importância da disciplina e da perseverança. A resposta correta é: {}.",
                    "A jornada rumo ao topo é pavimentada com desafios e superação. A resposta correta é: {}.",
                    "O conhecimento exige dedicação e investimento constante. A resposta correta é: {}.",
                    "O erro é um sinal para redobrar seus esforços e buscar aprimoramento. A resposta correta é: {}.",
                    "A resposta incorreta destaca a necessidade de aprimorar suas habilidades de análise. A resposta correta é: {}.",
                    "O sucesso é construído com base em esforço, disciplina e aprendizado constante. A resposta correta é: {}.",
                    "Não se deixe abater pelo erro, utilize-o como motivação para se superar. A resposta correta é: {}.",
                    "A resposta incorreta indica a necessidade de aprimorar suas estratégias de aprendizagem. A resposta correta é: {}.",
                    "O domínio do conhecimento exige rigor e precisão. A resposta correta é: {}.",
                    "A resposta incorreta evidencia a importância de se dedicar à busca pelo conhecimento. A resposta correta é: {}.",
                    "O caminho para o sucesso é árduo e exige persistência. A resposta correta é: {}.",
                    "A resposta incorreta serve como um alerta para intensificar seus estudos. A resposta correta é: {}.",
                    "O aprendizado exige foco e concentração para assimilar o conhecimento. A resposta correta é: {}.",
                    "A resposta incorreta destaca a importância de se dedicar à busca pela excelência. A resposta correta é: {}.",
                    "O caminho para o topo exige disciplina, esforço e constante aprimoramento. A resposta correta é: {}.",
                    "A resposta incorreta demonstra a necessidade de se dedicar com afinco aos estudos. A resposta correta é: {}.",
                ]
            },
            
            "Educado": {
                "correct_responses": [
                    "Excelente! Você está indo muito bem!",
                    "Que maravilha, você acertou!",
                    "Parabéns pela resposta correta!",
                    "Isso aí! Você tem um ótimo domínio do assunto.",
                    "É com grande satisfação que confirmo sua resposta correta!",
                    "Que bom ver seu progresso, continue assim!",
                    "Fico feliz em ver que você está aprendendo!",
                    "É inspirador ver sua dedicação aos estudos!",
                    "Sua resposta demonstra grande inteligência e conhecimento.",
                    "Continue com essa energia positiva, você está no caminho certo!",
                    "Você é um exemplo de aluno dedicado e perspicaz.",
                    "É admirável ver seu esforço em buscar conhecimento.",
                    "Sua resposta correta me enche de alegria!",
                    "Continue trilhando esse caminho de sucesso!",
                    "É gratificante ver você alcançar seus objetivos.",
                    "Sua inteligência e dedicação são inspiradoras!",
                    "Você me faz ter esperança no futuro da educação!",
                    "Que alegria poder celebrar seu sucesso!",
                    "É um prazer acompanhar seu desenvolvimento!",
                    "Parabéns por sua conquista, você merece!",
                    "Sua resposta demonstra grande capacidade de compreensão.",
                    "Você tem um futuro brilhante pela frente!",
                    "É recompensador ver você aplicar seus conhecimentos com maestria.",
                    "Continue buscando seus sonhos, você é capaz de alcançar grandes coisas!",
                    "Sua sede por conhecimento é inspiradora!",
                    "Você é um exemplo a ser seguido!",
                    "Que satisfação poder contribuir para sua jornada de aprendizado!",
                    "É um privilégio compartilhar esse momento de sucesso com você!",
                    "Parabéns por sua inteligência e dedicação!",
                    "Continue brilhando, o futuro te aguarda de braços abertos!"
                ],

                "incorrect_responses": [
                    "Não foi dessa vez, mas continue tentando! A resposta correta é: {}.",
                    "Que pena, você errou por pouco. A resposta correta é: {}.",
                    "Não desanime, errar faz parte do aprendizado. A resposta correta é: {}.",
                    "Com um pouco mais de atenção, você conseguirá acertar na próxima vez! A resposta correta é: {}.",
                    "Acredite em seu potencial, você é capaz de aprender e evoluir. A resposta correta é: {}.",
                    "Continue se esforçando, o sucesso é fruto de dedicação e persistência. A resposta correta é: {}.",
                    "O importante é não desistir, continue buscando conhecimento. A resposta correta é: {}.",
                    "Errar é humano, o importante é aprender com os erros. A resposta correta é: {}.",
                    "Com mais estudo e dedicação, você dominará o assunto. A resposta correta é: {}.",
                    "Não se preocupe, estamos aqui para te ajudar a aprender e crescer. A resposta correta é: {}.",
                    "Sua dedicação e esforço são admiráveis, continue se dedicando aos estudos. A resposta correta é: {}.",
                    "Errar é uma oportunidade para aprender e se fortalecer. A resposta correta é: {}.",
                    "Acredite em si mesmo, você é capaz de alcançar seus objetivos. A resposta correta é: {}.",
                    "Com paciência e persistência, você superará os desafios. A resposta correta é: {}.",
                    "O aprendizado é uma jornada, e errar faz parte do caminho. A resposta correta é: {}.",
                    "Confie em seu potencial, você pode chegar onde quiser. A resposta correta é: {}.",
                    "O importante é não desanimar, continue se dedicando aos estudos. A resposta correta é: {}.",
                    "Errar é uma oportunidade de aprendizado, não tenha medo de tentar novamente. A resposta correta é: {}.",
                    "Com esforço e dedicação, você dominará qualquer desafio. A resposta correta é: {}.",
                    "Acredite em si mesmo, você é capaz de realizar grandes coisas. A resposta correta é: {}.",
                    "Continue buscando conhecimento, a jornada de aprendizado é infinita. A resposta correta é: {}.",
                    "Errar é humano, o importante é aprender com as experiências. A resposta correta é: {}.",
                    "Com mais estudo e prática, você alcançará seus objetivos. A resposta correta é: {}.",
                    "Não se deixe abater pelos erros, use-os como motivação para se superar. A resposta correta é: {}.",
                    "O importante é continuar aprendendo e se desenvolvendo. A resposta correta é: {}.",
                    "Com dedicação e persistência, você superará qualquer obstáculo. A resposta correta é: {}.",
                    "Acredite em seu potencial, você é capaz de alcançar o sucesso. A resposta correta é: {}.",
                    "Continue se desafiando, o aprendizado é uma jornada constante. A resposta correta é: {}.",
                    "Errar faz parte do processo de aprendizado, o importante é seguir em frente. A resposta correta é: {}.",
                ]
            },
            "Normal": {
                "correct_responses": [
                    "Isso aí, acertou!",
                    "Boa, mandou bem!",
                    "Acertou em cheio!",
                    "É isso aí, continue assim!",
                    "Mandou bem pra caramba!",
                    "Você é fera, acertou de novo!",
                    "Que legal, você está afiado!",
                    "Muito bom, acertou mais uma!",
                    "Você está craque nesse assunto!",
                    "Acertou bonito!",
                    "Parabéns pela resposta correta!",
                    "Continue nesse ritmo, você está indo bem!",
                    "Você está mandando ver nesse quiz!",
                    "É isso aí, você está com tudo!",
                    "Legal demais, acertou mais uma!",
                    "Você está arrasando nesse quiz!",
                    "Mandou muito bem, continue assim!",
                    "Show de bola, você acertou!",
                    "Muito bom, você está aprendendo bastante!",
                    "Acertou, legal!",
                    "Você está pegando o jeito!",
                    "Muito bom, continue mandando bem!",
                    "Acertou, é isso aí!",
                    "Você está ficando bom nisso!",
                    "Ótimo, acertou mais uma!",
                    "Parabéns, você está indo muito bem!",
                    "Continue com essa energia, você está arrasando!",
                    "Legal, você acertou!",
                    "Muito bom, você está dominando o assunto!",
                    "Acertou, show!"
                ],
                "incorrect_responses": [
                    "Poxa, você errou! A resposta correta é: {}.",
                    "Tenta de novo, a resposta certa é: {}.",
                    "Quase! A resposta correta é: {}.",
                    "Não desanima, a resposta certa é: {}.",
                    "Errou feio! A resposta correta é: {}.",
                    "Na próxima você acerta! A resposta correta é: {}.",
                    "Putz, errou! A resposta correta é: {}.",
                    "Que pena, a resposta correta é: {}.",
                    "Não foi dessa vez! A resposta correta é: {}.",
                    "Errar é normal, a resposta correta é: {}.",
                    "Tenta de novo, quem sabe você acerta! A resposta correta é: {}.",
                    "Não desiste, a resposta certa é: {}.",
                    "Mais sorte na próxima! A resposta correta é: {}.",
                    "Uma pena, a resposta correta é: {}.",
                    "Valeu a tentativa! A resposta correta é: {}.",
                    "Quase lá! A resposta correta é: {}.",
                    "Continue tentando, a resposta certa é: {}.",
                    "Errou dessa vez! A resposta correta é: {}.",
                    "Na próxima você pega! A resposta correta é: {}.",
                    "Não foi dessa vez, mas não desanima! A resposta correta é: {}.",
                    "Tente outra vez, a resposta certa é: {}.",
                    "Continue praticando, a resposta correta é: {}.",
                    "Quase acertou! A resposta correta é: {}.",
                    "Errou por pouco! A resposta correta é: {}.",
                    "Mais sorte na próxima tentativa! A resposta correta é: {}.",
                    "Não desanime, a resposta correta é: {}.",
                    "Tenta de novo, você consegue! A resposta correta é: {}.",
                    "Continue se esforçando, a resposta correta é: {}.",
                    "Valeu a tentativa, a resposta correta é: {}.",
                    "Errou feio, mas não desanima! A resposta correta é: {}.",
                ]
            }
        }

    def build(self):
        self.profile_selection_layout = BoxLayout(orientation="vertical", spacing=30, padding=(50, 50))
        self.profile_label = Label(text="Selecione seu perfil:", size_hint=(1, 0.2), halign="center", font_size="24sp")
        self.rigid_button = Button(text="Rígido", on_press=lambda instance: self.start_quiz("Rígido"))
        self.polite_button = Button(text="Educado", on_press=lambda instance: self.start_quiz("Educado"))
        self.normal_button = Button(text="Normal", on_press=lambda instance: self.start_quiz("Normal"))
        self.profile_selection_layout.add_widget(self.profile_label)
        self.profile_selection_layout.add_widget(self.rigid_button)
        self.profile_selection_layout.add_widget(self.polite_button)
        self.profile_selection_layout.add_widget(self.normal_button)
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
        
        # Atualiza o root para o novo layout
        self.root.clear_widgets() 
        self.root.add_widget(self.layout) 

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
            self.layout.add_widget(Label(text=f"Parabéns, você acertou {self.correct_answers} de {len(self.questions)} perguntas!", halign="center", valign="middle", font_size="24sp"))

    def check_answer(self, instance):
        selected_option_index = self.answer_buttons.index(instance)
        question_data = self.questions[self.current_question_index]
        correct_option = question_data["correct_option"]
        selected_option_text = question_data["options"][selected_option_index]
        if selected_option_text == correct_option:
            self.correct_answers += 1
            content = Label(text=random.choice(self.profiles[self.profile]["correct_responses"]), halign="center", valign="middle")
        else:
            content = Label(text=random.choice(self.profiles[self.profile]["incorrect_responses"]).format(correct_option), halign="center", valign="middle")
        popup = Popup(title="Resposta", content=content, title_align="center", size_hint=(None, None), size=(600, 500))
        content.bind(size=content.setter('text_size'))
        popup.open()
        self.current_question_index += 1
        self.show_question()


if __name__ == "__main__":
    QuestionnaireApp().run()