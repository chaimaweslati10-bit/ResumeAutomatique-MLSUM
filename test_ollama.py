
import ollama

texte = """
L'intelligence artificielle transforme plusieurs secteurs,
notamment la médecine, l'éducation et les transports.
Elle permet d'automatiser certaines tâches et d'améliorer
les diagnostics médicaux.
"""

reponse = ollama.chat(
    model="qwen2.5:1.5b",
    messages=[
        {
            "role": "user",
            "content": "Résume ce texte en français en 2 phrases maximum : " + texte
        }
    ]
)

print("\nRésumé généré :")
print(reponse["message"]["content"])

