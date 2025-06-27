# snake_project/plotter.py

import matplotlib.pyplot as plt

plt.ion()

class Plotter:
    def __init__(self):
        self.scores = []
        self.mean_scores = []
        self.total_score = 0
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Progression de l\'entraînement')
        self.ax.set_xlabel('Nombre de Parties')
        self.ax.set_ylabel('Score')
        plt.show(block=False)

    def plot(self, new_score):
        self.scores.append(new_score)
        self.total_score += new_score
        mean_score = self.total_score / len(self.scores)
        self.mean_scores.append(mean_score)
        
        self.ax.cla()
        self.ax.set_title('Progression de l\'entraînement')
        self.ax.set_xlabel('Nombre de Parties')
        self.ax.set_ylabel('Score')
        self.ax.plot(self.scores, label='Score de la partie')
        self.ax.plot(self.mean_scores, label='Score moyen', linewidth=2)
        self.ax.set_ylim(bottom=0)
        self.ax.legend(loc='upper left')
        
        last_score_text = f"{self.scores[-1]}"
        last_mean_score_text = f"{self.mean_scores[-1]:.2f}"
        self.ax.text(len(self.scores) - 1, self.scores[-1], last_score_text, ha='center', va='bottom')
        self.ax.text(len(self.mean_scores) - 1, self.mean_scores[-1], last_mean_score_text, ha='center', va='bottom')
        
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.01)