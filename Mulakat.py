import tkinter as tk
import random
import json
from tkinter import messagebox

class SoruApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Soru Uygulaması")
        self.geometry("800x500")

        self.sorular = [
            {
                "soru": "Tell me about yourself.",
                "anahtar_kelimeler": "background, education, experience, skills"
            },
            {
                "soru": "What are your strengths?",
                "anahtar_kelimeler": "skills, abilities, achievements, examples"
            },
            {
                "soru": "What are your weaknesses?",
                "anahtar_kelimeler": "self-awareness, improvement, steps, progress"
            },
            {
                "soru": "Why do you want to work for our company?",
                "anahtar_kelimeler": "company values, culture, growth, opportunities"
            },
            {
                "soru": "What are your career goals?",
                "anahtar_kelimeler": "short-term, long-term, aspirations, development"
            },
            {
                "soru": "Why should we hire you?",
                "anahtar_kelimeler": "unique qualities, value, contributions, fit"
            },
            {
                "soru": "How do you handle stress and pressure?",
                "anahtar_kelimeler": "stress management, coping mechanisms, examples"
            },
            {
                "soru": "What is your greatest accomplishment?",
                "anahtar_kelimeler": "achievement, impact, skills demonstrated, story"
            },
            {
                "soru": "Describe a difficult work situation and how you overcame it.",
                "anahtar_kelimeler": "challenge, actions, result, lessons learned"
            },
            {
                "soru": "Do you have any questions for us?",
                "anahtar_kelimeler": "company culture, growth, expectations, team"
            },
            {
                "soru": "How do you handle failure?",
                "anahtar_kelimeler": "acceptance, learning, resilience, example"
            },
            {
                "soru": "What motivates you?",
                "anahtar_kelimeler": "inspiration, goals, achievements, growth"
            },
            {
                "soru": "What is your ideal work environment?",
                "anahtar_kelimeler": "culture, team, management style, work-life balance"
            },
            {
                "soru": "How do you prioritize tasks?",
                "anahtar_kelimeler": "time management, deadlines, importance, strategy"
            },
            {
                "soru": "What are your salary expectations?",
                "anahtar_kelimeler": "research, market value, experience, negotiation"
            },
            {
                "soru": "Describe a time when you had to work with a difficult team member.",
                "anahtar_kelimeler": "conflict resolution, communication, understanding, result"
            },
            {
                "soru": "What do you consider to be your greatest professional achievement?",
                "anahtar_kelimeler": "impact, recognition, skillset, example"
            },
            {
                "soru": "How do you stay updated on industry trends and developments?",
                "anahtar_kelimeler": "resources, networking, conferences, continuous learning"
            },
            {
                "soru": "How do you handle tight deadlines?",
                "anahtar_kelimeler": "prioritization, time management, focus, communication"
            },
            {
                "soru": "Describe a time when you had to deal with an unhappy customer or client.",
                "anahtar_kelimeler": "empathy, listening, problem-solving, outcome"
            },
            {
                "soru": "What type of work environment do you prefer?",
                "anahtar_kelimeler": "team, collaboration, structure, flexibility"
            },
            {
                "soru": "How do you stay organized?",
                "anahtar_kelimeler": "planning, tools, prioritization, routine"
            },
            {
                "soru": "Tell me about a time you had to learn something new quickly.",
                "anahtar_kelimeler": "adaptability, resourcefulness, learning, example"
            },
            {
                "soru": "How do you make decisions?",
                "anahtar_kelimeler": "analysis, intuition, collaboration, confidence"
            },
            {
                "soru": "Describe your communication style.",
                "anahtar_kelimeler": "clarity, active listening, adaptability, examples"
            },
            {
                "soru": "Tell me about a time you had to persuade someone.",
                "anahtar_kelimeler": "influence, negotiation, logic, example"
            },
            {
                "soru": "What is your leadership style?",
                "anahtar_kelimeler": "vision, motivation, delegation, adaptability"
            },
            {
                "soru": "How do you deal with change?",
                "anahtar_kelimeler": "flexibility, adaptability, learning, resilience"
            },
            {
                "soru": "What are your hobbies and interests outside of work?",
                "anahtar_kelimeler": "passions, balance, personal growth, networking"
            },
            {
                "soru": "What is your approach to problem-solving?",
                "anahtar_kelimeler": "critical thinking, creativity, collaboration, example"
            },
            {
                "soru": "How do you approach teamwork?",
                "anahtar_kelimeler": "collaboration, communication, support, example"
            },
            {
                "soru": "How do you handle criticism or feedback?",
                "anahtar_kelimeler": "openness, learning, improvement, example"
            },
            {
                "soru": "Tell me about a time you demonstrated initiative.",
                "anahtar_kelimeler": "proactivity, creativity, impact, example"
            },
            {
                "soru": "What experience do you have working remotely?",
                "anahtar_kelimeler": "tools, communication, discipline, adaptability"
            },
            {
                "soru": "What do you do when you don't know the answer to a problem?",
                "anahtar_kelimeler": "research, collaboration, resourcefulness, learning"
            },
            {
                "soru": "How do you ensure the quality of your work?",
                "anahtar_kelimeler": "attention to detail, standards, review, example"
            },
            {
                "soru": "Tell me about a time when you had to juggle multiple priorities.",
                "anahtar_kelimeler": "time management, prioritization, organization, example"
            },
            {
                "soru": "How do you stay motivated during repetitive tasks?",
                "anahtar_kelimeler": "goals, focus, variation, personal strategies"
            },
            {
                "soru": "What steps do you take to maintain a healthy work-life balance?",
                "anahtar_kelimeler": "boundaries, hobbies, self-care, time management"
            },
            {
                "soru": "Tell me about a time when you had to adapt your communication style.",
                "anahtar_kelimeler": "diversity, empathy, active listening, example"
            },
            {
                "soru": "What do you value most in a workplace?",
                "anahtar_kelimeler": "culture, teamwork, growth, work-life balance"
            },
            {
                "soru": "Tell me about a time when you had to deal with a challenging deadline.",
                "anahtar_kelimeler": "time management, prioritization, teamwork, example"
            },
            {
                "soru": "How do you continue learning and growing in your field?",
                "anahtar_kelimeler": "professional development, resources, curiosity, goals"
            },
            {
                "soru": "What strategies do you use to stay focused and productive?",
                "anahtar_kelimeler": "time management, organization, goals, environment"
            },
            {
                "soru": "How do you handle conflicts with colleagues?",
                "anahtar_kelimeler": "communication, empathy, resolution, example"
            },
            {
                "soru": "Tell me about a time when you had to manage multiple projects at once.",
                "anahtar_kelimeler": "organization, prioritization, communication, example"
            },
            {
                "soru": "What do you believe makes a great leader?",
                "anahtar_kelimeler": "vision, motivation, adaptability, communication"
            },
            {
                "soru": "How do you handle unexpected obstacles or challenges?",
                "anahtar_kelimeler": "adaptability, problem-solving, resilience, example"
            },
            {
                "soru": "Tell me about a time you went above and beyond for a project or task.",
                "anahtar_kelimeler": "initiative, dedication, impact, example"
            },
            {
                "soru": "How do you build relationships with team members and colleagues?",
                "anahtar_kelimeler": "communication, trust, collaboration, support"
            }
        ]

        self.favoriler = set()
        self.init_ui()
        self.load_notes()

    def init_ui(self):
        self.listbox = tk.Listbox(self, selectmode="single")
        self.listbox.pack(side="left", fill="both", expand=True)

        self.right_frame = tk.Frame(self)
        self.right_frame.pack(side="right", fill="both", expand=True)

        self.soru_label = tk.Label(self.right_frame, text="", wraplength=400)
        self.soru_label.pack(pady=10)

        self.anahtar_label = tk.Label(self.right_frame, text="", wraplength=400)
        self.anahtar_label.pack(pady=10)

        self.not_entry = tk.Text(self.right_frame, width=40, height=10) # Entry widget'ı yerine Text widget'ı kullanıldı.
        self.not_entry.pack(pady=10)

        self.kaydet_button = tk.Button(self.right_frame, text="Notu Kaydet", command=self.save_note)
        self.kaydet_button.pack(pady=10)

        self.getir_button = tk.Button(self.right_frame, text="Soru Getir", command=self.get_random_soru)
        self.getir_button.pack(pady=10)

        for index, soru in enumerate(self.sorular):
            self.listbox.insert(index, soru["soru"])

        self.listbox.bind("<<ListboxSelect>>", self.listbox_click)

    def load_notes(self):
        try:
            with open("notes.json", "r") as file:
                self.notes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.notes = {}

    def save_notes(self):
        with open("notes.json", "w") as file:
            json.dump(self.notes, file)

    def get_random_soru(self):
        soru = random.choice(self.sorular)
        self.show_soru(soru)

    def listbox_click(self, event):
        index = self.listbox.curselection()[0]
        soru = self.sorular[index]
        self.show_soru(soru)

    def show_soru(self, soru):
        self.current_soru = soru
        self.soru_label.config(text=soru["soru"])
        self.anahtar_label.config(text=soru["anahtar_kelimeler"])
        self.not_entry.delete(1.0, "end") # 1.0 ile başlangıç pozisyonu belirlendi.
        self.not_entry.insert(1.0, self.notes.get(soru["soru"], ""))

    def save_note(self):
        not_text = self.not_entry.get(1.0, "end-1c") # 1.0 ile başlangıç pozisyonu belirlendi ve "end-1c" ile son karakterin öncesine kadar alındı.
        self.notes[self.current_soru["soru"]] = not_text
        self.save_notes()

        messagebox.showinfo("Bilgi", "Not başarıyla kaydedildi!")
    

if __name__ == "__main__":
    app = SoruApp()
    app.mainloop()
