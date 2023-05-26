import openai

API_KEY = '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'
openai.api_key = API_KEY
model_id = 'gpt-3.5-turbo'


def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

conversation = []
prompt = 'imagine you are a expert in energy efficency, my global active power is 1000 watts give predictions. assume average is 10watts. give carbon foot print,i am in india,just give me a number,dont tell as an ai model stuff'
conversation.append({'role': 'user', 'content': prompt})
conversation = ChatGPT_conversation(conversation)
q = conversation[-1]['content'].strip()



from flask import Flask, request, render_template
import pickle


model = pickle.load(open('PCASSS_model.pkl', 'rb'))
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inspect", methods=["GET", "POST"])
def inspect():
    if request.method == "POST":
        GlobalReactivePower = float(request.form['GlobalReactivePower'])
        Global_intensity = float(request.form['Global_intensity'])
        Sub_metering_1 = float(request.form['Sub_metering_1'])
        Sub_metering_2 = float(request.form['Sub_metering_2'])
        Sub_metering_3 = float(request.form['Sub_metering_3'])
        x = [[GlobalReactivePower, Global_intensity, Sub_metering_1, Sub_metering_2, Sub_metering_3]]
        output = str(round(model.predict(x)[0], 3))
        conversation = []
        prompt = 'imagine you are a expert in energy efficency, my global active power is '+output+ 'watts give predictions. assume average is 10watts. give carbon foot print,i am in india,just give me a number,dont tell as an ai model stuff,dont tell statements like cant give a number etc'
        conversation.append({'role': 'user', 'content': prompt})
        conversation = ChatGPT_conversation(conversation)
        q = conversation[-1]['content'].strip()
        return render_template('output.html', output1=output,output2 = q)
    return render_template("inspect.html")

if __name__ == "__main__":
    app.run(debug=True)
