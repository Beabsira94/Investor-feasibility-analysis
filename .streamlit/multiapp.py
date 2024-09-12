import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        st.sidebar.title('Navigation')
        selection = st.sidebar.radio("Go to", [app["title"] for app in self.apps])

        for app in self.apps:
            if app["title"] == selection:
                app["function"]()
