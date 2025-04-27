# ©️ Créditos: #
Esse desafio foi feito no canal **"Spacelaxy"** no Discord. Todos os créditos à eles.<br/>
**Link: https://discord.gg/spacelaxy**. 

# Desafio "Protocolo Omega"

## 📖 História: 
Em 2026, depois de um colapso diplomático com a federação intergaláctica, a Terra foi marcada como um planeta de risco. A agência MIB acionou o protocolo Omega. Esse protocolo exige uma triagem global pra achar supostos aliens disfarçados de humanos. Você precisa replicar esse protocolo seguindo as seguintes regras:

---

## Objetivo:
O agente J solicitou que você criasse um relatório que retornasse uma tabela exatamente no seguinte modelo abaixo tanto em modelo de tabela quanto em modelo de objeto JSON, todos os dois modelos estão em ordem. 

**(exemplo do relatório (saída dos dados)):** nome | idade | planeta | língua | pontuação de risco | nível de risco | comportamentos mais frequentes | alien (true ou false) </br>

{
  "name": "Zarlon Mekk",
  "age": 153,
  "planet": "Xandar",
  "language": "Zorgonian",
  "riskScore": 10,
  "riskLevel": "Alto",
  "frequentBehaviors": ["Suspicious", "Aggressive"],
  "isAlien": true
}
</br>

---

## 🧐❓ O Que Fazer?

**Você deverá usar uma .JSON para carregar os dados que estão no repositório do desafio (link: [text](https://gist.github.com/henrythierrydev/81ced785d8471aa02078966195143c2a)).** 

**1** - Primeiro, você deve fazer uma validação se todos os dados estão presentes em cada coisa e também verificar o tipo dele. Por exemplo, o dado birthDate deve sempre estar no formato dia-mês-ano. Você **não** pode usar bibliotecas para isso e deve usar a File System para carregar todos os dados. Cada campo no objeto dos dados deve ser validado conforme o exemplo no final da descrição. </br>

**2** - A idade deve ser gerada com base na data de nascimento. </br>

**3** - Pra gerar a pontuação de risco, você precisa fazer uma lógica com algumas validações básicas, que são essas abaixo:
**3.1.** Caso o número de olhos seja acima ou igual a 4, então +3 pontos. </br>
**3.2.** Caso a altura seja maior que 2m, então adiciona +2 pontos. </br>
**3.3.** Caso ele fale Zorgonian, então adiciona +2 pontos. </br>
**3.4.** Caso ele tenha mais de 120 anos, então adiciona +3 pontos. </br>
**3.5.** Caso ele tenha tido algum comportamento no histórico de comportamentos que seja do tipo Suspicious, adiciona mais 2 pontos ou caso tenha tido um comportamento do tipo Aggressive, adiciona +2 pontos, ao mesmo tempo que se cada um se repetir 2 vezes no histórico, ignora totalmente a pontuação individual e adiciona +4 pontos. </br>

**4** - Já pra gerar o nível de risco, vamos primeiro definir os níveis que são: baixo, médio e alto. Cada nível de risco tem uma lógica que segue essa base:
**4.1.** **Baixo**: Entre 0 a 4 pontos. </br>
**4.2.** **Médio**: Entre 5 e 8 pontos. </br>
**4.3.** **Alto**: Acima de 8 pontos. </br>

**5** - Pra definir se ele é um alien ou não, vamos ter que procurar por **anomalias** e **padrões do comportamento**. Pra esse caso, vamos trabalhar também com numerações, que vão de 0 a 10, quanto mais próximo do 10, mais próximo de ser um alien você está:
**5.1.** Se tiver mais de 2 comportamentos como Suspicious, vamos adicionar +5 pontos. </br>
**5.2.** Os planetas Zebulon e Vega são as origens mais prováveis de alienígenas, já que todos os outros planetas incluindo a Terra são considerados como "da casa", então, caso ele venha de lá, +8 pontos. </br>
**5.3.** Caso ele não tenha marcas biológicas comuns entre todos os planetas da casa, então adiciona +6 pontos. </br>
**5.4.** Caso ele tenha mais ou menos de 2 olhos, então adiciona +2 pontos. </br>