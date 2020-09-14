from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.size = (300, 500)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            title: 'Kopi Gadang'
            left_action_items: [["menu",lambda x: app.navigation_draw()]]
            elevation: 10
        Image:
            source: 'Gadang.png'
            halign: 'center'

        MDBottomAppBar:
            MDToolbar: 
                title: 'Help'
                left_action_items: [["menu",lambda x: app.navigation_draw()]]
                mode: 'end'
                type: 'bottom'
                icon: 'coffee'  
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Kopi Gadang'                        
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                
                Image:
                    source: 'mine.jpg'
                MDLabel:
                    text: '   Aditya'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                MDLabel:
                    text: '    adit879ya@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Profil'                                                        
                        OneLineListItem:
                            text: 'Pesan'                            
                        OneLineListItem:
                            text: 'Tentang'
                        

"""

class KopiGadangApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'LightGreen'

        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("Navigation")

KopiGadangApp().run()