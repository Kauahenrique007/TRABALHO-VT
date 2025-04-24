from flask import Flask, render_template, json, abort
import os
from datetime import datetime

app = Flask(__name__)

# Configurações
app.config['PROJECTS_FILE'] = 'projects.json'
app.config['TEAM_FILE'] = 'team.json'

def load_json_data(filename):
    try:
        if not os.path.exists(filename):
            abort(500, description=f"Arquivo {filename} não encontrado")
            
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        return data
    except json.JSONDecodeError:
        abort(500, description=f"Erro ao ler arquivo {filename}")
    except Exception as e:
        abort(500, description=f"Erro interno: {str(e)}")

@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

@app.route("/")
def index():
    projects = load_json_data(app.config['PROJECTS_FILE'])
    team = load_json_data(app.config['TEAM_FILE'])
    
    # Encontra o projeto principal de IA
    main_project = next((p for p in projects if p.get('is_main')), None)
    
    return render_template(
        "index.html",
        projects=projects,
        team=team,
        main_project=main_project
    )

@app.route("/sobre")
def about():
    team = load_json_data(app.config['TEAM_FILE'])
    return render_template("about.html", team=team)

# ... (mantém os error handlers anteriores)