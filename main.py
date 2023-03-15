
import streamlit as st

contador = 0

def welcome():
    st.title("""Olá! Eu sou o db_chatbot de perfil de investidor.
    
    Eu posso ajudá-lo a descobrir qual é o seu perfil de investimento com base em algumas perguntas.
    """)

welcome()

respostas = []

perguntas = [
    ("Qual é o seu objetivo principal ao investir?<br>1) Preservação de capital<br>2) Geração de renda<br>3) Crescimento de capital"),
    ("Qual é o seu prazo de investimento?<br>1) Curto prazo (até 1 ano)<br>2) Médio prazo (de 1 a 5 anos)<br>3) Longo prazo (mais de 5 anos)"),
    ("Qual é a sua tolerância ao risco?<br>1) Baixa<br>2) Média<br>3) Alta"),
    ("Como você se sentiria em relação a perda de 10% de seu investimento?<br>1) Muito preocupado<br>2) Preocupado, mas disposto a esperar a recuperação<br>3) Indiferente"),
    ("Qual é a sua experiência anterior em investimentos?<br>1) Nenhuma<br>2) Pouca<br>3) Muita"),
    ("Qual é o seu conhecimento sobre o mercado financeiro?<br>1) Nenhum<br>2) Básico<br>3) Avançado"),
    ("Qual é a sua disponibilidade para acompanhar os seus investimentos?<br>1) Não tenho tempo<br>2) Algum tempo<br>3) Muito tempo"),
    ("Qual é a sua preferência de investimento?<br>1) Renda fixa<br>2) Renda variável<br>3) Ambos"),
    ("Qual é o seu patrimônio atual?<br>1) Mais de R$ 500.000,00<br>2) Entre R$ 100.000,00 e R$ 500.000,00<br>3) Menos de R$ 100.000,00"),
    ("Qual é a sua idade?<br>1) Mais de 50 anos<br>2) Entre 30 e 50 anos<br>3) Menos de 30 anos")
]
for i, pergunta in enumerate(perguntas):
    st.markdown(f"<h3 style='margin-top: 30px'>{pergunta}</h3>", unsafe_allow_html=True)
    respostas.append(st.number_input("Digite sua resposta (1, 2 ou 3):", min_value=1, max_value=3, step=1, key=f"q{i}"))
  
#st.write(respostas)
contador = (sum(respostas))* 5 /3
st.write(contador)

def perfil(contador):
    st.markdown("<h6>Com base nas suas respostas, seu perfil de investidor é:</h6>", unsafe_allow_html=True)
    st.write('')
    if contador > 0 and contador <= 20:
        st.markdown("<h2 style='color: #008000'>Perfil Conservador:</h2><p><h5>Investidor busca segurança em investimentos de baixo risco.</h5></p>", unsafe_allow_html=True)

    elif contador > 20 and contador <= 25:
      st.markdown("<h3 style='color: #FFA500'>Perfil Moderado:</h3><p><h5>Investidor busca equilíbrio entre segurança e rentabilidade.</h5></p>", unsafe_allow_html=True)

    elif contador > 25 and contador <= 35:
        st.markdown("<h3 style='color: #FFD700'>Perfil Moderado-Agressivo:</h3><p><h5>Investidor busca rentabilidade acima da média, sem assumir alto risco.</h5></p>", unsafe_allow_html=True)

    elif contador > 35 and contador <= 42:
        st.markdown("<h3 style='color: #FF8C00'>Perfil Agressivo:</h3><p><h5>Investidor busca rentabilidade acima de tudo, mesmo assumindo alto risco.</h5></p>", unsafe_allow_html=True)

    elif contador > 42 and contador <= 50:
        st.markdown("<h3 style='color: #FF0000'>Perfil Muito Agressivo:</h3><p><h5>Investidor busca rentabilidade acima de tudo, mesmo assumindo grandes perdas.</h5></p>", unsafe_allow_html=True)

perfil(contador)