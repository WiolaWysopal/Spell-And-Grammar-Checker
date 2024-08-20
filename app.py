from flask import Flask, request, render_template
from Model import SpellCheckerModule

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text', methods=['POST'])
def text_process():
    corrected_text = ""
    found_mistakes = ""
    if request.method == 'POST':
        text = request.form['text']
        if text:
            corrected_text, initial_mistakes = spell_checker_module.correct_spell(text)
            found_mistakes = ", ".join(f"{orig} - {corr}\n" for orig, corr in initial_mistakes) if initial_mistakes else "No mistakes found.\n"
        else:
            corrected_text = "No text provided."
            found_mistakes = "No text provided."
    return render_template('index.html', corrected_text=corrected_text, found_mistakes=found_mistakes)

@app.route('/file', methods=['POST'])
def file_process():
    corrected_file_text = ""
    found_file_mistakes = ""
    if request.method == 'POST':
        file = request.files['file']
        if file:
            readable_file = file.read().decode('utf-8', errors='ignore')
            # Skoryguj ortografię i zbierz informacje o błędach
            corrected_file_text, file_initial_mistakes = spell_checker_module.correct_spell(readable_file)
            all_mistakes = [f"{orig} - {corr}\n" for orig, corr in file_initial_mistakes]

            # Zastosuj korektę gramatyczną
            corrected_file_text, file_grammar_mistakes = spell_checker_module.correct_grammar(corrected_file_text)
            
            # Dołącz ewentuane błędy gramatyczne
            if file_grammar_mistakes and not isinstance(file_grammar_mistakes, str):
                all_mistakes.extend(f"{match[0]} - {match[1]}\n" for match in file_grammar_mistakes)

            # Komunikat do wypisania
            found_file_mistakes = ", ".join(all_mistakes) if all_mistakes else "No mistakes found.\n"
        else:
            corrected_file_text = "No file provided."
            found_file_mistakes = "No file provided."
    return render_template('index.html', corrected_file_text=corrected_file_text, found_file_mistakes=found_file_mistakes)

if __name__ == "__main__":
    app.run(debug=True)
