import flet as ft
from pygame import mixer
listen = 0
like = 0
musicnumber = 0
listonnumber = 0
redownload = 0
like2 = 0
playpath = ""
addname = ""

def main(page):
    mixer.init()
    page.title = "Main"
    page.window_frameless = True
    width=1285
    page.window_height=750
    page.window_resizable=True
    page.window_center()
    page.bgcolor="#ececec"
    page.fonts={
        "原耽与救赎": "main\原耽与救赎.原耽与救赎.ttf",
        "也字工厂爱的心电图": "main\也字工厂爱的心电图.ttf"
    }
    page.theme = ft.Theme(font_family="原耽与救赎")

    
    def fullscreentrue(e):
        page.window_full_screen = True
        page.update()
        

    def fullscreenfalse(e):
        page.window_full_screen = False
        page.update()

    def choose(e):
        can = e.control.selected_index
        if int(can) == 0:
            music.visible=True
            nomusicimg.visible=True
            number.visible=True
            add.visible=True
            add.update()
            music.update()
            number.update()
            nomusicimg.update()
            time.visible = True
            play.visible = True
            name.visible = True
            nm.visible = True
            love.visible = True
            back.visible = True
            img.visible = True
            back.update()
            time.update()
            play.update()
            name.update()
            nm.update()
            love.update()
            img.update()
        elif int(can) == 1:
            music.visible=False
            nomusicimg.visible=False
            number.visible=False
            add.visible=False
            add.update()
            music.update()
            number.update()
            nomusicimg.update()
            time.visible = True
            play.visible = True
            name.visible = True
            nm.visible = True
            love.visible = True
            back.visible = True
            img.visible = True
            time.update()
            play.update()
            name.update()
            nm.update()
            love.update()
            img.update()
            back.update()
        elif int(can) == 2:
            music.visible=False
            nomusicimg.visible=False
            number.visible=False
            add.visible=False
            add.update()
            music.update()
            number.update()
            nomusicimg.update()
            time.visible = True
            play.visible = True
            name.visible = True
            nm.visible = True
            love.visible = True
            img.visible = True
            back.visible = True
            time.update()
            play.update()
            name.update()
            nm.update()
            love.update()
            img.update()
            back.update()
        elif int(can) == 3:
            music.visible=False
            nomusicimg.visible=False
            number.visible=False
            add.visible=False
            add.update()
            music.update()
            number.update()
            nomusicimg.update()
            time.visible = True
            play.visible = True
            name.visible = True
            nm.visible = True
            back.visible = True
            love.visible = True
            img.visible = True
            time.update()
            play.update()
            name.update()
            nm.update()
            love.update()
            img.update()
            back.update()
        elif int(can) == 4:
            music.visible=False
            nomusicimg.visible=False
            number.visible=False
            add.visible=False
            add.update()
            music.update()
            number.update()
            nomusicimg.update()
            time.visible = False
            play.visible = False
            name.visible = False
            nm.visible = False
            love.visible = False
            back.visible = False
            img.visible = False
            time.update()
            play.update()
            name.update()
            nm.update()
            love.update()
            img.update()
            back.update()
        elif int(can) == 5:
            music.visible=False
            nomusicimg.visible=False
            number.visible=False
            add.visible=False
            add.update()
            music.update()
            number.update()
            nomusicimg.update()
            time.visible = False
            play.visible = False
            name.visible = False
            nm.visible = False
            love.visible = False
            back.visible = False
            img.visible = False
            time.update()
            play.update()
            name.update()
            nm.update()
            love.update()
            img.update()
            back.update()
        else:
            music.visible=False
            nomusicimg.visible=False
            number.visible=False
            add.visible=False
            add.update()
            music.update()
            number.update()
            nomusicimg.update()
            time.visible = False
            play.visible = False
            name.visible = False
            nm.visible = False
            love.visible = False
            img.visible = False
            back.visible = False
            time.update()
            play.update()
            name.update()
            nm.update()
            love.update()
            img.update()
            back.update()
        
    def addfavorite(e):
        global like
        like = like + 1
        if like % 2 != 0:
            love.selected = True
            love.update()
        else:
            love.selected = False
            love.update()
        
    def pause(e):
        global listen
        listen = listen + 1
        if listen % 2 != 0:
            mixer.music.play()
            play.selected = True
            play.update()
        else:
            mixer.music.pause()
            play.selected = False
            play.update()

    def liston(e):
        global listonnumber
        listonnumber = listonnumber + 1
        if listonnumber % 2 != 0:
            addlist.selected = True
            addlist.update()
        else:
            addlist.selected = False
            addlist.update()

    def downloadon(e):
        global redownload
        redownload = redownload + 1
        if redownload % 2 != 0:
            download.selected = True
            download.update()
        else:
            download.selected = False
            download.update()

    def addlove(e):
        global like2
        like2 = like2 + 1
        if like2 % 2 != 0:
            love2.selected = True
            love2.update()
        else:
            love2.selected = False
            love2.update()

    audio = ft.Audio(src="https://webfs.tx.kugou.com/202301081840/81f3582f328f89a69d53a1980d2fa739/v2/ada3847fed25fb93fd39fe0898dda24d/part/0/960171/KGTX/CLTX001/clip_ada3847fed25fb93fd39fe0898dda24d.mp3")
    page.overlay.append(audio)

    def addmusic(e: 
        ft.FilePickerResultEvent):
        if e.files:
            global addname
            music.value = "默认乐库"
            music.update()
            playpath = ", ".join(map(lambda m: m.path, e.files))
            mixer.music.load(playpath)
            print(playpath)
            addname = ", ".join(map(lambda f: f.name, e.files))
            addname = addname.strip(".mp3")
            musiclist.controls.append(
                ft.Container(
                    ft.Card(
                        ft.ListTile(
                            leading=ft.Image(src=choosesrc,width=35,height=35,fit=ft.ImageFit.FILL,border_radius=ft.border_radius.all(10),visible=True),
                            title=ft.Row([
                                ft.Text(f"{addname}",width=1000),
                                ft.IconButton(ft.icons.PLAY_ARROW_ROUNDED,on_click=playmusic),
                                
                            ]),
                            
                        )
                    )
                )
            )
        else:
            pass
        musiclist.update()

    def playmusic(e):
        global listen
        listen = 0
        listen = listen + 1
        play.selected = True
        play.update()
        print(addname)
        name.value = addname
        name.update()
        page.update()
        mixer.music.play()

        

        
    
    search = ft.TextField(label="在此处搜索...",width=600,height=32,prefix_icon=ft.icons.SEARCH,)
    #searchvalue = search.value()
    page.appbar = ft.AppBar(
        leading=ft.Row([ft.Icon(ft.icons.MUSIC_NOTE,size=25),ft.Text("MusicPlayer",)]),
        title=search,
        leading_width=50,
        center_title=True,
        bgcolor="#fdfdfd",
        toolbar_height=40,
        actions=[
            ft.Row([
            ft.IconButton(ft.icons.CIRCLE, on_click=fullscreenfalse,icon_color = "green",icon_size=20,width=20),
            ft.IconButton(ft.icons.CIRCLE, on_click=fullscreentrue,icon_color = "yellow",icon_size=20,width=20),
            ft.IconButton(ft.icons.CIRCLE, on_click=lambda _: page.window_close(),icon_color = "red",icon_size=20,width=40),
            ])
        ]
    )
    rail = ft.NavigationRail(
        selected_index = 0,
        width=50,
        bgcolor="#ececec",
        group_alignment=-1,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.PLAY_ARROW,
                selected_icon_content=ft.Icon(ft.icons.PLAY_ARROW_OUTLINED),
                label_content=ft.Text("播放"),
                           
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.PLAYLIST_PLAY,
                selected_icon_content=ft.Icon(ft.icons.PLAYLIST_PLAY_ROUNDED),
                label_content=ft.Text("歌单"),           
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_OUTLINE,
                selected_icon_content=ft.Icon(ft.icons.FAVORITE),
                label_content=ft.Text("最爱"),           
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.DOWNLOAD_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOWNLOAD),
                label_content=ft.Text("下载"),           
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.MORE_HORIZ_ROUNDED,
                selected_icon_content=ft.Icon(ft.icons.MORE_HORIZ_ROUNDED),
                label_content=ft.Text("信息"),           
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.CODE,
                selected_icon_content=ft.Icon(ft.icons.TERMINAL),
                label_content=ft.Text("源码"),           
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("设置"),
            ),
            
        ],
        on_change=choose
        
    )

    choosesrc = "https://y.qq.com/music/photo_new/T002R300x300M000000uz9wv2w1EkD_2.jpg?max_age=2592000"
    nomusic = "https://y.qq.com/music/photo_new/T002R300x300M0000030lak94GN5Ad_0.jpg?max_age=2592000"
    test = ft.TextField(label="test",visible=False)
    img = ft.Image(src=choosesrc,width=80,height=80,fit=ft.ImageFit.FILL,border_radius=ft.border_radius.all(10),visible=True)
    nomusicimg = ft.Image(src=nomusic,width=130,height=130,fit=ft.ImageFit.FILL,border_radius=ft.border_radius.all(10),visible=True)
    musiclist = ft.Row(wrap=True,scroll="hidden",expand=True,width=1190,)
    startplay = ft.IconButton(ft.icons.PLAY_ARROW_ROUNDED,)
    love = ft.IconButton(ft.icons.FAVORITE_BORDER,icon_size=25,selected_icon=ft.icons.FAVORITE,selected_icon_color="red",on_click=addfavorite)
    love2 = ft.IconButton(ft.icons.FAVORITE_BORDER,icon_size=25,selected_icon=ft.icons.FAVORITE,selected_icon_color="red",on_click=addlove)
    time = ft.ProgressBar(width=1165,color="green",value=0)
    name = ft.Text(value="no")
    music = ft.Text("当前没有音乐,请添加",size=30)
    number = ft.Text(str(musicnumber) + "首",size=25)
    back = ft.IconButton(ft.icons.SKIP_PREVIOUS_ROUNDED,icon_size=30)
    play = ft.IconButton(ft.icons.PLAY_CIRCLE_ROUNDED,icon_size=30,selected_icon=ft.icons.PAUSE_CIRCLE_ROUNDED,selected_icon_color="black",on_click=pause)
    nm = ft.IconButton(ft.icons.SKIP_NEXT_ROUNDED,icon_size=30)
    addmusicdectory = ft.FilePicker(on_result=addmusic,)
    add = ft.FilledTonalButton("添加音乐", icon="add",on_click=lambda _:addmusicdectory.pick_files(allowed_extensions=["mp3"],))
    download = ft.IconButton(ft.icons.DOWNLOAD_ROUNDED,selected_icon=ft.icons.FILE_DOWNLOAD_DONE,on_click=downloadon,selected_icon_color="black")
    addlist = ft.IconButton(ft.icons.PLAYLIST_ADD_OUTLINED,selected_icon=ft.icons.PLAYLIST_ADD_CHECK,on_click=liston,selected_icon_color="black")

    page.overlay.append(addmusicdectory)
    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1,),
                ft.Column([
                    ft.Row([
                        nomusicimg,
                        ft.Column([    
                            music,                       
                            ft.Row([
                                number,add,
                            ]),
                            
                        ]),
                        
                        ]),
                        musiclist,
                ])
                
                
            ],
            expand=True,
        ),
        test,
        ft.Row([
            img,
            ft.Column([
                name,time,ft.Row([
                    back,
                    play,
                    nm,
                    download,
                    addlist,
                    love,
                ]),
            ]),
            
        ])
        
    )

    '''    
    if searchvalue == "":
        name.value = "当前没有待播放的歌曲."
        name.update()
    else:
        name.value = search.value()
        name.update()
    '''

    '''for i in range(10):
        musiclist.controls.append(
            ft.Container(
                ft.Card(
                    ft.ListTile(
                        leading=ft.Image(src=choosesrc,width=35,height=35,fit=ft.ImageFit.FILL,border_radius=ft.border_radius.all(10),visible=True),
                        title=ft.Row([
                            ft.Text(f"{i}",width=950),
                            startplay,
                            download,
                            addlist,
                            love2,
                        ]),

                    )
                )
            )
        )'''
        
     
    
            
    page.update()


ft.app(target=main)
