from shiny import App, ui, render

# Define UI
app_ui = ui.page_fluid(
    ui.h2(" Interactive Greeting App ", style='padding:20px; padding-left: 0px;'),
    
    ui.input_text("name", "Enter your name:", placeholder="Type here..."),
    
    ui.input_select("color", "Pick a background color:", 
                    {"white": "White", "#FFD700": "Gold", "#87CEEB": "Sky Blue", "#90EE90": "Light Green"}),
    
    ui.output_ui("greeting"),
)

# Define Server Logic
def server(input, output, session):

    @output
    @render.ui
    def greeting():
        name = input.name().strip()
        color = input.color()
        
        greeting_text = f"<h2>Hello, {name}! 👋</h2>" if name else "<h2>Hello, World! 🌎</h2>"
        
        return ui.HTML(f"<div style='padding:20px;  padding-left: 0px; width: fit-content; border-radius:10px; background-color:{color};'>{greeting_text}</div>")

# Create Shiny App
app = App(app_ui, server)
