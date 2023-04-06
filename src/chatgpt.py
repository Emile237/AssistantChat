import openai

class ChatGPT:
    """
    Cette classe représente un assistant conversationnel basé sur la technologie de traitement du langage naturel
    GPT-3 de OpenAI.

    Args:
        api_key (str): La clé d'API OpenAI.
        model (str, optional): Le nom du modèle GPT-3 à utiliser. Par défaut, "gpt-3.5-turbo" est utilisé.

    Attributes:
        model (str): Le nom du modèle GPT-3 utilisé par l'assistant.
        api_key (str): La clé d'API OpenAI utilisée par l'assistant.
        messages (list): Une liste des messages échangés entre l'utilisateur et l'assistant, stockés sous la forme
            d'un dictionnaire contenant le rôle de l'émetteur et le contenu du message.

    Methods:
        add_message(role, content): Ajoute un message à la liste des messages échangés.
        get_response(user_message): Obtient la réponse de l'assistant à un message d'utilisateur donné.
    """

    def __init__(self, api_key, model="gpt-3.5-turbo"):
        """
        Initialise une instance de la classe ChatGPT.

        Args:
            api_key (str): La clé d'API OpenAI.
            model (str, optional): Le nom du modèle GPT-3 à utiliser. Par défaut, "gpt-3.5-turbo" est utilisé.
        """
        self.model = model
        self.api_key = api_key
        openai.api_key = self.api_key
        self.messages = [{"role": "system", "content": "Vous êtes un assistant utile."}]

    def add_message(self, role, content):
        """
        Ajoute un message à la liste des messages échangés.

        Args:
            role (str): Le rôle de l'émetteur du message (soit "user" pour l'utilisateur, soit "assistant" pour
                l'assistant).
            content (str): Le contenu du message.
        """
        self.messages.append({"role": role, "content": content})

    def get_response(self, user_message):
        """
        Obtient la réponse de l'assistant à un message d'utilisateur donné.

        Args:
            user_message (str): Le message de l'utilisateur.

        Returns:
            str: La réponse de l'assistant au message de l'utilisateur.
        """
        self.add_message("user", user_message)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        assistant_message = response.choices[0].message['content']
        self.add_message("assistant", assistant_message)
        return assistant_message
