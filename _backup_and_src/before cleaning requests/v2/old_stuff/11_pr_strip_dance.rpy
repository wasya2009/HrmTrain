    
##################################################################################################################################
### LEVEL 04 #####################################################################################################################
###################REQUEST_11 (Level 04) (DANCE FOR ME AND SNAPE) (Day/Night) ################################################################
label new_request_11: #LV.4 (Whoring = 9 - 11)
    #__#hide screen hermione_main 
    #__#with d3
    $herView.hideQQ()
   
    m "{size=-4}(Попросить её станцевать для вас?){/size}"

    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request

    $ current_payout = 35 #Because will have option to pay extra.

    if request_11_points == 0: #<==============================EVENT 01
        
        m "Мисс Грейнджер, не могли бы вы станцевать для меня."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        $ pos = POS_140
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_11.png", pos )
        her "Вы хотите, чтобы я..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_10.png", pos )
        her "...танцевала для вас, сэр?"
        if whoring <= 8:
            jump too_much
        $ new_request_11_01 = True # HEARTS
        m "Да... как вы думаете, вы сможете справиться с этим?"
        her "Эм... Я попробую..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_11.png", pos )
        her "Это ваше официальное предложение, сэр?"
        with hpunch
        g4 "Что ты сказала!?"
        stop music fadeout 1.0
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_12.png", pos )
        her "Я имею в виду, пользу. Это в пользу школы сэр?"
        show screen whitetone8
        hide screen blktone
        with Dissolve(1)
        #__#hide screen hermione_main
        $herView.hideQ( Dissolve( 1 ) )
        #__#with Dissolve(1)
        g4 "(\"Это ваше официальное желние, мастер....?\")"
        m "(О, это  вызывает воспоминания...)"
        m "(Аграба и Джини...)"
        m "(Пре-акабурная эра моей жизни...)"
        m "(Неплохие времена...)"
        g4 "(Сволочь, испортил мне жизнь!)"
        her "Eм... Профессор?"
        hide screen whitetone8
        with Dissolve(1)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( None, pos )
        call music_block
        her "сэр..?"
        m "Так Гермиона..."
        m "Я предался воспоминаниям..."
        her "Я получу за это награду?"
        m "Конечно, девочка!"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_29.png", pos )
        her "Так... я просто немного потанцую..."
        m "Начинай, когда будешь готова..."
        her "................."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        ">Гермиона начинает танцевать..."
        stop music fadeout 1.0
        hide screen blktone
        $ hermione_chibi_xpos = 400 #Near the desk.
        #$ hermione_chibi_ypos = 240 #Default: 250
        show screen clothed_dance #Hermione stands still.
        with fade
        m "Хм..."
        #__#her_12 "{size=-5}(...........................................){/size}"
        $her_head_state = 12
        her_head_main "{size=-5}(...........................................){/size}"
        #__#her_04 "{size=-5}(Это глупо...){/size}"
        $her_head_state = 4
        her_head_main "{size=-5}(Это глупо...){/size}"
        ">Гермиона выглядит растерянной, но она продолжает \"танцы\"..."
        m "..................."
        #__#her_04 "{size=-5}(...........................................){/size}"
        her_head_main "{size=-5}(...........................................){/size}"
        m "Отлично, теперь можешь начинать раздеваться."
        show screen hermione_02 #Hermione stands still.
        with hpunch
        #__#her_07 "??!"
        $her_head_state = 7
        her_head_main "??!"
        #__#her_08 "Мы же договаривались только о танце?"
        $her_head_state = 8
        her_head_main "Мы же договаривались только о танце?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "В самом деле? Вот обидно."
        m "Теперь начинай снимать свою одежду."
        #__#her_12 "Вы хотете чтобы я станцевала вам стриптиз...?"
        $her_head_state = 12
        her_head_main "Вы хотите, чтобы я станцевала вам стриптиз...?"
        m "Да. И я ожидаю, что ты сделаешь это сегодня, девочка."
        #__#her_19 "Профессор Дамблдор!"
        $her_head_state = 19
        her_head_main "Профессор Дамблдор!"
        m "Не повышай свой голос на меня, девочка!"
        #__#her_07 ".....!!?"
        $her_head_state = 7
        her_head_main ".....!!?"
        m "Никто не заставляет вас делать это."
        m "Я делаю вам одолжение!"
        m "Если вам не нужны очки, пожалуйста, не задерживайтесь в кабинете."
        #__#her_08 "....................."
        $her_head_state = 8
        her_head_main "....................."
        #__#her_12 "......................................."
        $her_head_state = 12
        her_head_main "......................................."
        ">Гермиона начинает танцевать снова..."
        show screen clothed_dance #Hermione stands still.
        with fade
        #__#her_15 "{size=-5}(...........................................){/size}"
        $her_head_state = 15
        her_head_main "{size=-5}(...........................................){/size}"
        m "Чего же вы ждете?"
        m "Начните с жилета."
        #__#her_12 "............................................................."
        $her_head_state = 12
        her_head_main "............................................................."
        ">Гермиона на миг растерянно замирает, а затем снимает с себя жилет..."
        show screen ctc
        pause
        show screen no_vest_dance
        with d3
        pause
        #__#her_19 "{size=-5}(Я действительно собираюсь сделать это?){/size}"
        $her_head_state = 19
        her_head_main "{size=-5}(Я действительно собираюсь сделать это?){/size}"
        menu:
            m "......................."
            "\"Теперь избавься от юбки!\"":
                #__#her_19 "................................."
                her_head_main "................................."
                show screen blktone
                with d3
                ">Гермиона начинает растегивать свою юбку..."
                ">Она очень смущена, поэтому у нее это сразу не получается..."
                ">Наконец, молния расстегнута и у нее нет выбора, кроме как снять юбку..."
                hide screen blktone
                with d3
                #__#her_19 "{size=-5}(Вот и она...){/size}"
                her_head_main "{size=-5}(Вот и она...){/size}"
                #__#her_24 "{size=-5}(За честь \"Гриффиндора\"....){/size}"
                $her_head_state = 24
                her_head_main "{size=-5}(За честь \"Гриффиндора\"....){/size}"
                ">Гермиона сняла свою юбку..."
                show screen ctc
                pause
                show screen no_skirt_dance
                with d3
                pause
                m "..............."
                #__#her_19 "{size=-5}(.........................................){/size}"
                $her_head_state = 19
                her_head_main "{size=-5}(.........................................){/size}"
                ">Гермиона продолжает танцевать..."
                m "Ладно, рубашка следующая!"
                #__#her_20 "Моя рубашка....?"
                $her_head_state = 20
                her_head_main "Моя рубашка....?"
                show screen blktone
                with d3
                ">Гермиона выглядит крайне неловко..."
                ">Она неуклюже копошится с пуговицами рубашки..."
                hide screen blktone
                with d3
                m "В чем проблема, девочка?"
                #__#her_19 "Мне жаль, сэр..."
                $her_head_state = 19
                her_head_main "Мне жаль, сэр..."
                #__#her_19 "Оно застряло..."
                her_head_main "Пуговица застряла..."
                #__#her_19 "И не хочет выйти..."
                her_head_main "И не хочет расстегиваться..."
                #__#her_28 "Почему не двигается?! *хлюп*"
                $her_head_state = 28
                her_head_main "Почему она не расстегивается?! *хлюп*"
                #__#her_28 "Нет,я не могу сделать этого, сэр! *хлюп*"
                her_head_main "Нет, я не могу сделать этого, сэр! *хлюп*"
                m "Что?"
                #__#her_28 "Я думал, я мог бы, но..."
                her_head_main "Я думала, я смогу, но..."
                #__#her_28 "Станцевать стриптиз, сэр?"
                her_head_main "Станцевать стриптиз, сэр?"
                #__#her_28 "Люди смотрят на меня в этой школе!"
                her_head_main "Люди равняются на меня в этой школе!"
                #__#her_28 "У меня репутация...*хлюп*"
                her_head_main "У меня репутация...*хлюп*"
                #__#her_29 "And if I do this..."
                $her_head_state = 29
                #__#her_head_main "And if I do this..."
                her_head_main "И если я сделаю это..."
            "\"Сейчас же сними рубашку!\"":
                #__#her_19 "................................."
                $her_head_state = 19
                her_head_main "................................."
                show screen blktone
                with d3
                ">Гермиона начинает расстегивать свою рубашку..."
                ">Она, кажется, очень нерешительой и тянет время..."
                ">Наконец, последняя пуговица снята, и у нее нет выбора, кроме как снять рубашку..."
                hide screen blktone
                with d3
                #__#her_19 "{size=-5}(Ладно,показываю...){/size}"
                her_head_main "{size=-5}(Ладно, снимаю...){/size}"
                #__#her_19 "{size=-5}(За честь \"Гриффиндора\"!){/size}"
                her_head_main "{size=-5}(За честь \"Гриффиндора\"!){/size}"
                show screen blktone
                with d3
                ">Гермиона сняла с себя рубашку..."
                hide screen blktone
                with d3
                show screen ctc
                pause
                show screen no_shirt_dance
                with d3
                pause
                #__#her_40 "{size=-5}(Я сделала это...){/size}"
                $her_head_state = 40
                her_head_main "{size=-5}(Я сделала это...){/size}"
                #__#her_40 "{size=-5}(Профессор Дамблдор видит мою грудь пока я танцую...){/size}"
                her_head_main "{size=-5}(Профессор Дамблдор видит мою грудь пока я танцую...){/size}"
                #__#her_40 "{size=-5}(Это так унизительно...){/size}"
                her_head_main "{size=-5}(Это так унизительно...){/size}"
                #__#her_40 "{size=-5}(Но я делаю это для моего факультета...){/size}"
                her_head_main "{size=-5}(Но я делаю это для моего факультета...){/size}"
                m "Неплохо...."
                #__#her_40 "{size=-5}(.........................................){/size}"
                her_head_main "{size=-5}(.........................................){/size}"
                show screen blktone
                with d3
                ">Гермиона топлес..."
                ">Она продолжает танцевать, но, кажется, она очень стеснена в движениях. Даже больше, чем раньше..."
                ">Похоже, она отчаянно пытается предотвратить покачивания и подпрыгивания её груди.."
                hide screen blktone
                with d3
                m "Ладно, юбка следующая!"
                #__#her_40 "...................."
                her_head_main "...................."
                show screen blktone
                with d3
                ">Гермиона выглядит крайне растерянной..."
                show screen blktone8
                with d3
                ">Она пытается расстегнуть молнию на юбке..."
                m "Какие-то проблемы, девочка?"
                #__#her_40 "Мне жаль, сэр..."
                her_head_main "Мне жаль, сэр..."
                #__#her_40 "Она застраляа..."
                her_head_main "Она застряла..."
                #__#her_40 "Не сдвигается..."
                her_head_main "Не двигается..."
                #__#her_40 "Почему она не двигается *всхлип*"
                her_head_main "Почему она не двигается? *всхлип*"
                #__#her_41 "Нет, Я не могу, сэр! *всхлип*"
                $her_head_state = 41
                her_head_main "Нет, я не могу, сэр! *всхлип*"
                m "Что?"
                #__#her_41 "Я думала, что смогу, но..."
                her_head_main "Я думала, что смогу, но..."
                #__#her_41 "Стриптиз за очки, сэр?"
                her_head_main "Стриптиз за очки, сэр?"
                #__#her_41 "Люди ровняются на меня в этой школе!"
                her_head_main "Люди равняются на меня в этой школе!"
                #__#her_41 "У меня есть репутация...*всхлип*"
                her_head_main "У меня есть репутация...*всхлип*"
                #__#her_42 "И если я это сделаю..."
                $her_head_state = 42
                her_head_main "И если я это сделаю..."
                
        show screen blkfade 
        with d3
        hide screen blktone8    
        ">Гермиона быстро одевает свою форму..."
        stop music fadeout 1.0
        show screen hermione_02 #Hermione stands still.
        hide screen blkfade
        with d3
        #__#her_31 "сэр, я думаю мне стоит уйти... *всхлип!*"
        $her_head_state = 31
        her_head_main "Сэр, я думаю мне стоит уйти... *всхлип!*"
        menu:
            "\"Ладно. Мне было весело. Вот твои очки.\"":
                #__#$ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $herView.setZOrder( 8 )
                #__#$ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                #__#$ h_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ pos = gMakePos( 390, 340 )
                #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                #__#show screen hermione_main
                $herView.showQ( "body_13.png", pos ) #"WARNING_Z"
                her2 "Правда? Я ничего не испортила?"
                #__#hide screen hermione_main
                $herView.hideQ() #"WARNING_Z"
                pause.2 #Otherwise a bug occurs. 
                #__#$ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $herView.setZOrder( 5 )
                #__#$ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ pos = gMakePos( 390, 0 )
            "\"Конечно. И ты не получишь очки.\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                #__#$ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $herView.setZOrder( 8 )
                #__#$ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                #__#$ h_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ pos = gMakePos( 390, 340 )
                #__#$ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
                #__#show screen hermione_main
                $herView.showQ( "body_02.png", pos ) #"WARNING_Z"
                her2 "сэр... Мне кажется, я не очень хороша в этом..."
                her2 "НО я сделала все, что смогла... Я думаю, я заслужила--"
                #__#hide screen hermione_main
                $herView.hideQ() #"WARNING_Z"
                m "Просто в следующий раз постарайтесь лучше, Мисс Грейнджер."
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                #__#show screen hermione_main
                $herView.showQ( "body_31.png", pos ) #"WARNING_Z"
                her2 "Следующий раз?!"
                $herView.hideQ() #WARNING_Z
                #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                $herView.showQ( "body_47.png", pos )
                her2 "Уверяю вас, сэр, следующего раза не будет..."
                #__#hide screen hermione_main
                $herView.hideQ() #"WARNING_Z"
                m "Посмотрим..."
                #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                #__#show screen hermione_main
                $herView.showQ( "body_66.png", pos ) #"WARNING_Z"
                her2 "Арх!"
                #__#hide screen hermione_main
                $herView.hideQ() #"WARNING_Z"
                pause.2 #Otherwise a bug occurs. 
                #__#$ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $herView.setZOrder( 5 )
                #__#$ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ pos = gMakePos( 390, 0 )
                $ mad += 35
                call music_block
                jump could_not_flirt

    # SECOND PART #

    if request_11_points == 1: #<====================================================================================================================EVENT 02 
        $ new_request_11_02 = True # HEARTS
        m "Мисс Грейнджер, я хочу, чтобы вы станцевали для меня."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        $ pos = POS_140
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_66.png", pos )
        her "Снова, сэр...?"
        m "Все будет оплачено, конечно же..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_69.png", pos )
        her "............................"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_69.png", pos )
        her "И вы ожидаете от меня... Эм..."
        m "Стриптиз, конечно же"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_69.png", pos )
        stop music fadeout 1.0
        her "......................"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_66.png", pos )
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "Ну, почему бы и нет?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_86.png", pos )
        her "Да, и правда, почему бы и нет!"
        m "Хм...? {size=-4}(Посмотрите на нее. Такая энергичная...){/size}"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_30.png", pos )
        her "В конце концов, как ученица, я должна подчиняться любому вашему приказу, не так ли, сэр?!"
        m "...................."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_30.png", pos )
        her "Если директор говорит мне раздеться, то, значит, я сделаю это!!!"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_47.png", pos )
        her "Даже если это неуместно, позорно и унизительно?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_30.png", pos )
        her "Конечно же это не так. Какой вздор!"
        m ".............."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_47.png", pos )
        her "Ха! Все ведь так, как и должно быть!"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        hide screen blktone 
        with d3
        m "??!"
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
        pause 5
        g4 "!!!!!!"
        ">К вашему удивлению, Гермиона взбирается на ваш стол и начинает безумно танцевать..."
        hide screen blkfade
        $ hermione_chibi_xpos = 210 #Near the desk: 400.
        $ hermione_chibi_ypos = 180 #Default: 250
        show screen clothed_dance #Hermione stands still.
        show screen ctc
        with fade
        pause
        show screen bld1
        show screen blktone
        with d3
        #__#$ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
        $herView.setZOrder( 8 )
        #__#$ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        #__#$ h_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
        $ pos = gMakePos( 390, 340 )
        #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Flashing Трусики
        #__#show screen hermione_main
        $herView.showQ( "body_30.png", pos ) #"WARNING_Z"
        her2 "Я должна немного опуститься, чтобы защитить честь своего факультета..."
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        ">Гермиона начинает снимать свой жилет..."
        #__#$ h_body = "03_hp/13_hermione_main/body_86.png" #Flashing Трусики
        #__#show screen hermione_main
        $herView.showQ( "body_86.png", pos ) #"WARNING_Z"
        her "Пусть все так и будет!"
        $herView.hideQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Flashing Трусики
        $herView.showQ( "body_87.png", pos )
        her "Просто..."
        $herView.hideQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_88.png" #Flashing Трусики
        $herView.showQ( "body_88.png", pos )
        her "*стон*"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        show screen blktone8
        hide screen blktone
        with d3
        ">Ее жилет, кажется, застрял. Но она рьяно продолжает пытаться его снять..."
        #__#show screen hermione_main
        $herView.showQ( None, pos )
        her "Почему он не....?!"
        $herView.hideQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_81.png" #Flashing Трусики
        her "Вот!"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        ">Гермионе наконец удается стянуть жилет и она кидает его в другую часть комнаты..."
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        show screen no_vest_dance
        with d3
        pause
        show screen bld1
        with d3
        #__#show screen hermione_main
        $herView.showQ( "body_81.png", pos )
        hide screen ctc
        #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Flashing Трусики
        her "Юбка следующая, да?"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
       
        menu:
            m "..."
            "\"Да, именно. Снимай ее!\"":
                #__#show screen hermione_main
                $herView.showQ( None, pos )
                her "Конечно!"
                #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Flashing Трусики
                $herView.addFaceName( "body_87.png" ) #WARNING_Z
                her "А вот и она!"
                #__#hide screen hermione_main
                $herView.hideQ() #"WARNING_Z"
                pause.1
                show screen blktone8
                with d3
                ">Гермиона бросает свою юбку через всю комнату, как сделала это с жилетом ранее..."
            "\"Успокойся, девочка. \"":
                #__#show screen hermione_main
                $herView.showQ( None, pos )
                her2 "Ну, {size=+7}ПРОСТИТЕ МЕНЯ{/size}, профессор!"
                her2 "Вы попросили меня станцевать стриптиз для вас, но не предупреждали, насколько громкой я должна быть!"
                #__#hide screen hermione_main
                $herView.hideQ() #"WARNING_Z"
                m "Ну, я говорю это сейчас!"
                #__#show screen hermione_main
                $herView.showQ( None, pos )
                her2 "Слишком поздно!"
                #__#hide screen hermione_main
                $herView.hideQ() #"WARNING_Z"
                pause.1
                show screen blktone8
                with d3
                ">И она бросает свою юбку через всю комнату, как сделала это с жилетом ранее..."
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        show screen no_skirt_dance
        with d3
        pause
        show screen bld1
        with d3
        hide screen ctc
        m "{size=-4}(Вау, она и правда поработала над этим...){/size}"
        m "{size=-4}(Может быть, еще рано для-{/size}"
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" 
        #__#show screen hermione_main
        $herView.showQ( "body_66.png", pos ) #"WARNING_Z"
        her "Моя рубашка?!!"
        #__#$ h_body = "03_hp/13_hermione_main/body_86.png" 
        her "{size=+9}Мне она не нужна!{/size}"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        pause.1
        show screen blktone8
        with d5
        ">Ее рубашка внезапно падает на пол."
        g4 "{size=-4}(Когда она успела??!){/size}"
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        show screen no_shirt_no_skirt_dance
        with d3
        pause
        show screen bld1
        with d3
        #__#show screen hermione_main
        $herView.showQ( "body_86.png", pos )
        hide screen ctc
        her "Вам нравится, сэр?"
        #__#$ h_body = "03_hp/13_hermione_main/body_30.png" 
        her2 "Мне стоит потрясти сиськами, как одна из тех шлюх?"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        m "Ну---"
        #__#show screen hermione_main
        $herView.showQ( "body_30.png", pos )
        her2 "Конечно! Почему бы мне не опуститься для вашего же удовольствия?!"
        #__#$ h_body = "03_hp/13_hermione_main/body_86.png" 
        $herView.addFaceName( "body_86.png" )
        her2 "Это вполне {size=+7}приемлемо!{/size}"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        pause.1
        show screen blktone
        with d3
        ">Гермиона начинает неуклюже трясти своими сиськами..."
        ">Пока вы смотрите? как сиськи этой девочки расскачиваются то влево, то в право, вам приходится бороться с сильным желанием..."
        menu:
            m "..."
            "- Схватить их! -":
                g9 "{size=-4}(Да, просто положить свои руки на эти милые сиськи, именно!){/size}"
                g9 "{size=-4}(Может? чуть подергать их...){/size}"
            "- Шлепнуть! -":
                m "{size=-4}(О да, хочу шлепнуть их.){/size}"
                g9 "{size=-4}(Да, просто немного шлепнуть...){/size}"
            "- Укусить!":
                m "{size=-4}(Это странно, что я хочу впиться в них зубами?){/size}"
                m "{size=-4}(Нет, это не странно!){/size}"
                m "{size=-4}(Просто пара нежных укусов с любовью!){/size}"
                g9 "{size=-4}(Да... Может быть? больше чем пара...){/size}"
            "- Зарыться в них лицом! -":
                m "{size=-4}(Я просто хочу залезть лицом между ними!){/size}"
                g9 "{size=-4}(Да, зарыться в них лицом это лучшее, что можно сделать!){/size}"
        ">Пока вы думаете, Гермиона продолжает танцевать..."
        
        #__#$ badges = False # Turns off the badges layer.
        $herView.hideItem( 'dress' )
        #__#$ h_body = "03_hp/13_hermione_main/body_89.png" 
        #__#$ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
        $herView.setZOrder( 8 )
        $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ h_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
        $ pos = gMakePos( h_xpos, h_ypos )
        #__#show screen hermione_main
        $herView.showQ( "body_89.png", pos )
        her2 "(Танцую голой перед директором...)"
        her2 "(Если бы мои родители узнали об этом, они бы просто сошли с ума...)"
        #__#$ h_body = "03_hp/13_hermione_main/body_90.png"
        her2 "(Особенно отец...)"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        ">Гермиона снова трясет своими грудками...)"
        #__#show screen hermione_main
        $herView.showQ( "body_90.png", pos )
        her "(Гермиона Грейнджер - стриптизерша...)"
        #__#$ h_body = "03_hp/13_hermione_main/body_91.png"
        her2 "(Прости меня, папочка...)"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        pause.1
        show screen blktone8
        hide screen blktone
        with d3
        ">Гермиона кладет свои руки на грудь и начинает сжимать ее..."
        ">Вы можете только предполагать, что у нее на уме, но выглядит она очень подавленно и стыдливо."
        #__#show screen hermione_main
        $herView.showQ( "body_91.png", pos )
        her2 "(Я лучший студент... Я являюсь примером для других...)"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        ">Гермиона сильнее хватается за сиськи и скручивает их пару раз..."
        ">Выглядит так, будто она зла на них и пытается наказать..."
        ">Вы находите это странным..."
        #__#$ h_body = "03_hp/13_hermione_main/body_92.png"
        #__#show screen hermione_main
        $herView.showQ( "body_92.png", pos ) #"WARNING_Z"
        $ h_c_u_pic = "03_hp/08_animation_02/05_panties_01.png"
        show screen h_c_u
        her "Ну, я думаю, вам это нравится, сэр!"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        m "Что?"
        #__#$ h_body = "03_hp/13_hermione_main/body_93.png"
        #__#show screen hermione_main
        $herView.showQ( "body_93.png", pos ) #"WARNING_Z"
        her "Я хотела бы получить оплату..."
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        m "Вы ничего не забыли, Мисс Грейнджер?"
        #__#$ h_body = "03_hp/13_hermione_main/body_92.png"
        #__#show screen hermione_main
        $herView.showQ( "body_92.png", pos ) #"WARNING_Z"
        her2 "сэр...?"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        m "Ваши трусики...?"
        #__#$ h_body = "03_hp/13_hermione_main/body_94.png"
        #__#show screen hermione_main
        $herView.showQ( "body_94.png", pos ) #"WARNING_Z"
        her "Мои трусики?"
        her "Но, они всегда остаются!"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        m "Когда это \"всегда\"?"
        m "Стриптиз в детских мультиках?"
        m "Стриптиз это стриптиз, девочка!"
        m "Теперь, снимай свои трусики!"
        #__#$ h_body = "03_hp/13_hermione_main/body_95.png"
        #__#show screen hermione_main
        $herView.showQ( "body_95.png", pos ) #"WARNING_Z"
        her "................"
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        ">Гермиона выглядит испуганно. Вся ее злоба ушла..."
        #__#$ h_body = "03_hp/13_hermione_main/body_90.png"
        #__#show screen hermione_main
        $herView.showQ( "body_90.png", pos ) #"WARNING_Z"
        her "................."
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
        ">Не говоря ни слова..."
        ">Она начинает снимать свои трусики..."
        g9 "......................................."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
        $ walk_xpos=470 #Animation of walking chibi. (From)
        $ walk_xpos2=360 #Coordinates of it's movement. (To)
        hide screen blktone8
        hide screen bld1
        show screen snape_walk_01 
        with d3
        pause 1.5
        stop music 
        $ renpy.play('sounds/scratch.wav')
        show screen snape_02 #Snape stands still.
        
        $ tt_xpos=330 #Defines position of the Snape's full length sprite. (Default 300). 140 - center.
        $ tt_ypos=340#(Default 0). Right bottom corner: 340
        $ s_sprite = "03_hp/10_snape_main/snape_01.png"
        #__#$ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box. Works for all full size sprites.
        $herView.setZOrder( 8 )
        show screen s_head
        $ h_c_u_pic = "03_hp/08_animation_02/05_panties_01.png"
        show screen h_c_u
        
        # WARNING_Z
        
        sna2 "Послушай, Джинни. Я тут подумал--"
        $ s_sprite = "03_hp/10_snape_main/snape_11.png"
        with hpunch
        sna2 "................................................................................................................................................................................"
        $ h_body = "03_hp/13_hermione_main/body_96.png"
        show screen h_head
        with hpunch
        her "(Профессор Снейп???????!)"
        $ s_sprite = "03_hp/10_snape_main/snape_12.png"
        show screen s_head
        sna2 "Мисс Грейнджер?"
        show screen h_head
        her "(Нет, нет... Этого нельзя допустить. Пожалуйста...)"
        hide screen h_head
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "...................................."
        show screen bld1
        with d3
        menu:
            m "..."
            "\"Северус, Я сейчас занят.\"":
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna "Да... Я вижу..."
                $ h_body = "03_hp/13_hermione_main/body_97.png"
                show screen h_head
                her "{size=-7}(Я хочу сдохнуть!){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_12.png"
                show screen s_head
                sna2 "Отложим наш разговор на потом, Джинн-- *Кхм!* Альбус."
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                sna "Мисс Грейнджер..."
                $ h_body = "03_hp/13_hermione_main/body_97.png"
                show screen h_head
                her ".........................................."
                hide screen h_head
            "\"Северус! Пожалуйста, присоеденяйся.\"":
                $ mad += 37
                $ snape_invated_to_watch = True #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
                $ s_sprite = "03_hp/10_snape_main/snape_14.png"
                show screen s_head
                sna "Серьезно?"
                $ h_body = "03_hp/13_hermione_main/body_97.png"
                show screen h_head
                her "(Профессор, нет, пожалуйста.............................)"
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna "Действительно, заманчивое предложение..."
                $ h_body = "03_hp/13_hermione_main/body_95.png"
                show screen h_head
                her "!!!!!!......."
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna2 "Ну, может вдругой раз..."
                $ h_body = "03_hp/13_hermione_main/body_99.png"
                show screen h_head
                her "{size=-5}(Другого раза не будет!){/size}"
                her "{size=-5}(Клянусь, я перестану продавать себя за эти гребаные очки!){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_12.png"
                show screen s_head
                sna2 "Отложим наш разговор, Джинн-- *Кхм!* Альбус."
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                sna2 "Мисс Грейнджер..."
                $ h_body = "03_hp/13_hermione_main/body_97.png"
                show screen h_head
                her "................................."
                hide screen h_head
        show screen blkfade 
        with d3
        hide screen snape_walk_01 
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        pause 1.5

        
        ">Снейп уходит..."
        ">Гермиона спешно спрыгивает с вашего стола."
        ">Она отчаянно пытается натянуть на себя одежду..."
        $ h_body = "03_hp/13_hermione_main/body_98.png"
        show screen h_head
        her "Моя рубашка! Где моя рубашка?!"
        hide screen h_head
        m "Там, у камина..."
        $ h_body = "03_hp/13_hermione_main/body_85.png"
        show screen h_head
        her2 "................................"
        hide screen h_head
        pause 2
        $ h_body = "03_hp/13_hermione_main/body_33.png"
        show screen h_head
        
        $ badges = True # Turns the badges layer back ON.
        
        her "........................"
        $ h_body = "03_hp/13_hermione_main/body_34.png"
        stop music fadeout 2.0
        her "Могу я получить свои очки, пожалуйста?"
        hide screen h_head
        hide screen snape_02 #Snape stands still.
        pause.1
        #__#$ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box. On top of EVERYTHING = 8.
        $herView.setZOrder( 5 )
        $ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
        $ hermione_chibi_xpos = 400 #Near the desk.
        show screen hermione_02 #Hermione stands still.
        $ hermione_chibi_ypos = 250 #Default: 250. Another number is 180
            
            
    # THIRD PART #
            
    if request_11_points >= 2: #<====================================================================================================================EVENT 03
        $ new_request_11_03 = True # HEARTS
        if snape_invated_to_watch: #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
            m "(Хм... могу ли я позвать Снейпа тоже посмотреть на это?)"
            menu:
                "\"Да! Гермионе нужна аудитория!\"":
                    if not invited_snape_once_already:
                        $ invited_snape_once_already = True #Makes sure this event takes place only once.
                        hide screen blktone
                        with d3
                        m "Мисс Грейнджер, Я хочу от вас еще одну услугу сегодня."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        $ pos = gMakePos( h_xpos, h_ypos )
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_16.png", pos )
                        her "Конечно, сэр."
                        m "Но для начала, вы не могли бы пойти и позвать профессора Снейпа сюда?"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_17.png", pos )
                        her "...Профессора Снейпа?"
                        her "Могу я спросить, зачем, сэр?"
                        m "Ох, Я думаю, вам нужна большая аудитория для подобных танцев."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_48.png", pos )
                        her "Подобных танцев...?!!"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_47.png", pos )
                        her "Со всем уважением, сэр..."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_07.png", pos )
                        her "{size=-5}(Которого уже и так мало...){/size}"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_30.png", pos )
                        her "Я отказываюсь унижаться перед профессором Снейпом!"
                        m "Нет, нет. Ты поняла все не так."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_15.png", pos )
                        her "Хм..?"
                        m "Я хочу проверить профессор Снейпа на причастность к \"грязным\" делишкам с помощью тебя."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_48.png", pos )
                        her "!!!"
                        m "Да, хочу поймать его на месте преступления!"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_11.png", pos )
                        her "Профессор, Я не понимаю..."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_06.png", pos )
                        her "Теперь ясно..."
                        her "Я извиняюсь, что засомневалась в вас, сэр..."
                        m "Ничего. Теперь найди профессор Снейпа и приведи его сюда."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_111.png", pos )
                        her "Как скажете, сэр!"
                        label fetching_snape:
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        hide screen bld1
                        with d3
                        hide screen hermione_02 #Hermione stands still.
                        $ walk_xpos=400 #Animation of walking chibi. (From)
                        $ walk_xpos2=610 #Coordinates of it's movement. (To)
                        $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                        show screen hermione_walk_01_f 
                        pause 2
                        hide screen hermione_walk_01_f 
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        with Dissolve(.3)
                        pause.2
                        show screen blkfade
                        with d5
                        stop music fadeout 1.0
                        ">...................{w}...................{w}...................{w}..................."
                        hide screen blkfade
                        with d5
                        $ walk_xpos=610 #Animation of walking chibi. (From)
                        $ walk_xpos2=360 #Coordinates of it's movement. (To)
                        $ snapes_speed = 04.0 #The speed of moving the walking animation across the screen.
                        show screen snape_walk_01 
                        
                        pause 4
                        show screen snape_02 #Snape stands still.

                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        $ hermione_chibi_xpos = 610
                        $ hermione_chibi_ypos = 250
                        show screen hermione_02 #Hermione stands still.
                        with Dissolve(.5)
                        pause.3
                        
                        $ walk_xpos=610 #Animation of walking chibi. (From)
                        $ walk_xpos2=500 #Coordinates of it's movement. (To) 400 - near desk.
                        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                        show screen hermione_walk_01 
                        pause 3
                        $ hermione_chibi_xpos = 500 #Near the desk - 400
                        show screen hermione_02 #Hermione stands still.
                        pause.5
                        show screen ctc
                        pause
                        show screen bld1
                        with Dissolve(.3)
                        $ tt_xpos=180 #Defines position of the Snape's full length sprite. Default - 300
                        $ tt_ypos=0
                        $ s_sprite = "03_hp/10_snape_main/snape_01.png"
                        show screen snape_main
                        show screen ctc
                        with Dissolve(.3)
                        
                    else:
                        hide screen blktone
                        with d3
                        m "Мисс Грейнджер, Я хочу от вас еще одну услугу сегодня."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        $ pos = POS_140
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_16.png", pos )
                        her "Конечно, сэр."
                        m "Но для начала, вы не могли бы пойти и позвать профессора Снейпа сюда?"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_17.png", pos )
                        her "...Профессор Снейп?"
                        her "Могу я спросить, зачем, сэр?"
                        m "Ох, я просто хочу, чтобы ты станцевала для нас."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_14.png", pos )
                        her "!!!"
                        m "Я хочу проверить профессора Снейпа на причастность к \"грязным\" делишкам и ты должна мне помочь."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_29.png", pos )
                        her "Но разве мы не договаривались, что я делаю это в последний раз?"
                        m "Ну, Эм... конечно..."
                        m "Но мне нужны доказательства, если я хочу отправить это в министерство магии!"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_47.png", pos )
                        her "....."
                        m "Ну, что ты скажешь, девочка?"
                        m "Один танец для большей справедливости?"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_66.png", pos )
                        her "Ну, ладно..."
                        m "Отлично. Тогдай пойди и найди профессора Снейпа."
                        jump fetching_snape
                    
                    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                    sna "Джинни... э-э, то есть Альбус, ты хотел видеть меня?"
                    m "Да. Не желаешь немного стриптиза?"
                    hide screen snape_main
                    with d3
                    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
                    show screen snape_main
                    with d3
                    sna "Оу...?"
                    sna "Мисс Гейнджер будет выступать, не так ли?"
                    #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    $ h_xpos=380 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    $ pos = gMakePos( h_xpos, h_ypos )
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_34.png", pos )
                    her ".............."
                    m "Да, наша маленькая потаскуха будет более чем довольна снять одежду для нас."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    #__#$ h_xpos=380 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_34.png", pos )
                    her "............"
                    m "Не так ли, девочка?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    #__#$ h_xpos=380 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_34.png", pos )
                    her "Да, сэр."
                    m "В таком случае, приступай!"
                    #__#hide screen hermione_main
                    $herView.hideQ() #"WARNING_Z"
                    hide screen snape_main
                    
                    pause
                    
                    show screen blkfade
                    with Dissolve(1)
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 1
                    $ h_body = "03_hp/13_hermione_main/body_16.png"
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    show screen h_head2
                    her2 "............."

                    
                    
                    $ s_head_xpos = 330 # x = 330,
                    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.
                    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
                    show screen s_head2
                    sna "......................"
                    hide screen s_head2
                    m ".........................."
                    hide screen blkfade
                    hide screen bld1
                    $ hermione_chibi_xpos = 210 #Near the desk: 400.
                    $ hermione_chibi_ypos = 180 #Default: 250
                    show screen clothed_dance #Hermione stands still.
                    show screen ctc
                    show screen s_c_u
                    $ s_c_u_pic = "03_hp/09_snape_ani/snape_0130.png"
                    $ snape_chibi_xpos = 290 #Default 360.
                    $ snape_chibi_ypos = 210
                    with fade
                    pause
                    show screen bld1
                    with d3
                    m "И так... Северус... Как жизнь?"
                    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
                    show screen s_head2
                    sna "Ну, вы знаете ... все по старому, все по старому..."
                    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
                    sna " Студенты вызывают одно разочарование..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    sna2 "На самом деле, Мисс Грейнджер удалось достать меня больше остальных..."
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_68.png"
                    her "..............................."
                    hide screen h_head2
                    m "Я уверен, она очень сожалеет об этом..."
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_74.png"
                    her "{size=-4}(Ни капельки!){/size}"
                    hide screen h_head2
                    m "И сделает что угодно для тебя сегодня, да, девочка?"
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_53.png"
                    her "Э-эм... Да, профессор."
                    hide screen h_head2
                    hide screen ctc
                    pause.2
                    show screen blktone
                    with d3
                    ">Гермиона снимает свой жилет и начинает покачивать бедрами."
                    hide screen blktone
                    with d3

                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_vest_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_87.png"
                    her "..................."
                    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
                    show screen s_head2
                    sna "Хм... В последнее время ты очень тихая."
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_48.png"
                    her "{size=-4}(О нет! Он дейстивтельно так считает?){/size}"
                    $ h_body = "03_hp/13_hermione_main/body_57.png"
                    her2 "Я просто делаю то, что мне сказал профессор..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Сегодня вы не собираетесь читать мне лекции о \"коррупкции в Хогвартсе\"?"
                    hide screen s_head2
                    m "Северус..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Неь, Альбус, я хочу услышать ответ от нашей маленькой мисс совершенство."
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_57.png"
                    her2 "Я просто хочу, чтобы вы отлично провели время, сэр..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Ох! Этот \"сэр\", это ведь не ко мне ты обращаешься?"
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
                    sna2 "Что стало с  \"Снейпо-каракулем\" и профессором \"Сопливикусом\"!??"
                    hide screen s_head2
                    g9 "{size=-5}( \"Сопливикус\", хех... это забавно.){/size}"
                    show screen h_head2 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_57.png" # HERMIONE
                    her "............."
                    $ s_sprite = "03_hp/10_snape_main/snape_08.png"
                    show screen s_head2
                    sna2 "Да, я знаю, как ты зовешь меня за спиной, девочка!"
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_86.png"
                    her2 "Может быть это потому что вы заслужили это... сэр."
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Что?!"
                    sna "Да как ты смеешь....?"
                    $ s_sprite = "03_hp/10_snape_main/snape_15.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Кем ты себя возомнила? Ты грязно--"
                    show screen h_head2 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_62.png" # HERMIONE
                    her2 "Профессор, один из ваших сотрудников собирается оскорбить меня!"
                    her2 "Вы это допустите?"
                    $ s_sprite = "03_hp/10_snape_main/snape_08.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Оскорблять...?! Ты очень нервируешь меня, девочка!"
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna2 "Альбус, ты позволишь ей так разговаривать с учителем?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_62.png" # HERMIONE
                    her "Профессор Дамблдор!"
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Альбус!"
                    hide screen s_head2
                    menu:
                        m "..."
                        "\"Мисс Грейнджер, проявите уважение!\"":
                            $ mad += 9
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_61.png" # HERMIONE
                            her "Что?"
                            her "Но профессор!"
                            hide screen h_head2  
                            m "Юная леди, вам {size=+4}следует{/size} успокоиться."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_66.png" # HERMIONE
                            her "Арх!"
                            hide screen h_head2      
                            m "И снимай свою юбку, хорошо?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "......."
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "..........."
                            hide screen s_head2  
                        "\"Северус, ты первый начал.\"":
                            $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                            show screen s_head2  
                            sna "Что? Я?!"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_52.png" # HERMIONE
                            her "Спасибо, профессор."
                            $ s_sprite = "03_hp/10_snape_main/snape_08.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Albus, ты портишь девочку! Ей нужно преподать урок!"
                            hide screen s_head2 
                            m "...............Северус."
                            g4 "Ты головой ударился?!"
                            $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Простите?"
                            hide screen s_head2 
                            g4 "Она танцует стриптиз для тебя!"
                            g4 "О каком наказании идет речь?"
                            $ s_sprite = "03_hp/10_snape_main/snape_16.png" #SNAPE
                            show screen s_head2  
                            sna "Арх... Как насчет порки?" 
                            hide screen s_head2
                            g4 "Северус!"
                            $ s_sprite = "03_hp/10_snape_main/snape_17.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Ладно, ладно, я понял тебя..."
                            hide screen s_head2
                            m "Мисс Грейнджер, вы собиретесь танцевать для нас или подняться как можно выше, чтобы получить лучший вид сверху?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                            her "Эм..."
                            hide screen h_head2
                            m "Снимай свою юбку, девочка!"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "Да, сэр..."
                            hide screen h_head2
                        "\"Вы оба, заткнитесь нахер.\"":
                            m "Ты, высокий-темный-парень, успокойся, ага?"
                            $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Простите?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "Да! Вы должны сказать ему--"
                            hide screen h_head2     
                            m "И ты тоже, извращенка!"
                            m "Успокойтесь и снимайте с себя уже юбку."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_79.png" # HERMIONE
                            her "Я не извращенка..."
                            hide screen h_head2     
                            m "Юбка, девочка!"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "......"
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2  
                            sna "............."
                            hide screen s_head2     
                    
                    show screen blktone
                    with d3
                    ">Гермиона быстро снимает юбку \"Хогвартса\"..."
                    hide screen blktone
                    with d3
                   
                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_skirt_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    show screen s_head2
                    sna "Хм..."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                    her "........................"
                    hide screen h_head2
                    m "Да, так-то лучше!"
                    show screen blktone
                    with d3
                    ">Гермиона продолжает танцевать. На ней уже не осталось ничего, кроме рубашки..."
                    menu:
                        m "..."
                        "\"Северус, что насчет Поттера?\"":
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "(.....?)"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2
                            sna "Что с ним?"
                            hide screen s_head2
                            m "Ты все еще из за него расстраиваешься?"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "О..."
                            sna "На самом деле нет."
                            $ s_sprite = "03_hp/10_snape_main/snape_06.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Честно говоря у меня никогда не было с ним особых проблем..."
                            sna2 "Хотя я планировал сделать его жизнь невыносимой из-за его отца..."
                            $ s_sprite = "03_hp/10_snape_main/snape_02.png" #SNAPE
                            show screen s_head2    
                            sna2 "Но в последнее время у меня есть много интересных проектов, чтобы занять себя..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "..................."  
                            hide screen h_head2   
                        "\"Северус, что насчет семьи Уизли?\"":
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Что с ними?"
                            hide screen s_head2   
                            m "Они все еще являются проблемой?"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да... Больше чем раньше."
                            hide screen s_head2
                            m "Хм...?"
                            m "Ты кажешься удивительно равнодушным насчет этого..."
                            $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Это только потому что я знаю что в конце концов они получат то, что заслуживают..."
                            hide screen s_head2
                            m "Месть? Отлично! Что у тебя на уме?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "!!!"
                            $ s_sprite = "03_hp/10_snape_main/snape_06.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Хм... Can't discuss this with \"the enemy\" present."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "Арх!"
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Все что я могу сказать - это то, что это включает в себя их любимую маленькую сестренку Джинни..."
                            hide screen s_head2  
                            m "Джинни? Хм... Что за странное имя для девочки..."
                            m "............."
                            m "Так ты планируешь ее трахнуть?"
                            $ s_sprite = "03_hp/10_snape_main/snape_08.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "!!?"
                            $ s_sprite = "03_hp/10_snape_main/snape_17.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Альбус, пожалуйста, не перед девочкой же!"
                            hide screen s_head2  
                            m "Хорошо, хорошо..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                            her "{size=-5}(Ginny...){/size}"
                            hide screen h_head2 
                        "\"Как ты оцениваешь попку Гермионы?\"":
                            $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "ягодицы мисс Гермионы?" 
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "!!!............"
                            hide screen h_head2      
                            m "Конечно! Так же, как ты оцениваешь бумагу."
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Хм..."
                            hide screen s_head2  
                            pause.1
                            ">Профессор Снейп оценивающе смотрит на ягодицы Гермионы..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
                            her ".........?"
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Я бы сказал..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_59.png" # HERMIONE
                            her "............?!"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да... \"{size=+5}F-{/size}\"."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                            her "(Что?!)"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Неудовлетворительно..."
                            sna2 "Посмотрите на это. Маленькая и тощая... Да это задница мальчика."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_51.png" # HERMIONE
                            her "!!!!!!!!!!"
                            hide screen h_head2   
                            
                    show screen blktone
                    with d3
                    ">Одну за другой, Гермиона расстегивает пуговицы своей блузки и снимает ее..."
                    hide screen blktone
                    with d3
                   
                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_shirt_no_skirt_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    m "Неплохо! Мы наконец-то добрались до приятного!"
                    $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                    show screen s_head2       
                    sna "Хм..."
                    
                    $ badges = False # Hides the layer with badges.
                    
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_90.png" # HERMIONE
                    her "........"
                    hide screen h_head2   
                    menu:
                        m "..."
                        "- Начать дрочить -":
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            
                            hide screen bld1
                            show screen ctc
                            with d3
                            pause
                            show screen blkfade
                            with d6
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_94.png"
                            her "Профессор Дамблдор?!"
                            hide screen h_head2
                            m "Все в порядке, девочка. Не возражай мне..."
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "О, мы будем теперь вести себя так?"
                            sna "Что же, не обращай внимания, если я начну..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_94.png" # HERMIONE
                            $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.
                            her "!!!"
                            hide screen h_head2    
                            
                            
                            hide screen genie
                            hide screen no_shirt_no_skirt_dance
                            $ genie_chibi_xpos = -185
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "jerking_off_02_ani"
                            $ snape_chibi_xpos = -185
                            $ snape_chibi_ypos = 10
                            $ s_c_u_pic = "jerking_off_03_ani" #Snape.
                            show screen chair_02
                            show screen g_c_u
                            show screen desk_02
                            show screen no_shirt_no_skirt_dance
                            hide screen blkfade
                            with fade
                            pause
                            show screen bld1
                            with d3
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_95.png"
  
                            her "Нет, ребята... эмм, я имею в виду сэры... Эм, профессоры!"
                            hide screen h_head2
                            m "Не обращай внимания на нас, девочка, просто продолжай."
                            show screen h_head2
                            her "Но..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_99.png" # HERMIONE
                            her2 "Нет! Я отказываюсь танцевать, пока эти штуки нацелены на меня!"
                            her2 "Вы должны убрать их, или танца не будет!"
                            hide screen h_head2    
                            m "Ты не в том положении, чтобы что-то требовать, девочка."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_110.png" # HERMIONE
                            her2 "это было не требование, сэр.Это был ультиматум."
                            hide screen h_head2    
                            menu:
                                m "..."
                                "\"Что же Северус, давай будем цивилизованными...\"":
                                    $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                                    show screen s_head2                                                          #SNAPE
                                    sna2 "Я вижу Мисс Грейнджер может вести себя упорно в любой ситуации..."
                                    hide screen s_head2  
                                    show screen blkfade
                                    with d3
                                    hide screen no_shirt_no_skirt_dance
                                    show screen genie
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk_02
                                    show screen no_shirt_no_skirt_dance
                                    show screen s_c_u
                                    $ s_c_u_pic = "03_hp/09_snape_ani/snape_0130.png"
                                    $ snape_chibi_xpos = 290 #Default 360.
                                    $ snape_chibi_ypos = 210
                                    pause.3
                                    hide screen blkfade 
                                    with d3
                                    jump civil_with_snape
                                    
                                "\"(Пст! Напомните мне, зачем мы это делаем!)\"":
                                    if whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_104.png" # HERMIONE
                                        her "О, точно..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Что это было?"
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_108.png" # HERMIONE
                                        her "Пожалуйста, не возражайте против меня..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Хм...?"
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_108.png" # HERMIONE
                                        her2 "Я не против, что вы трогаете себя передо мной..."
                                        her2 "Да, я не против всего этого..."
                                        her "Я просто продолжу танцевать..."
                                        hide screen h_head2
                                        hide screen ctc
                                        pause.1
                                        show screen blktone
                                        with d3
                                        show screen blktone8
                                        with d3
                                        ">Вы продолжаете дрочить, смотря на танец Гермионы..."
                                        ">Гермиона сжимает свою грудь и немного покачивает бедрами..."
                                        hide screen blktone8
                                        with d3
                                        m "Да, ммм. Очень хорошо."
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "*Кхм!* Неплохое выступление, Мисс Грейнджер."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_97.png" # HERMIONE
                                        her "...................."
                                        hide screen h_head2
                                        m "Хех..."
                                        hide screen h_head2
                                        m "Как вы оцените ее грудь?"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_94.png" # HERMIONE
                                        her "......"
                                        $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Хм......"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_103.png" # HERMIONE
                                        her "........"
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "\"4+\"!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_94.png" # HERMIONE
                                        her "!!!"
                                        hide screen h_head2
                                        m "Правда?"
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Да. Я всегда отдаю должное."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_90.png" # HERMIONE
                                        her "(Профессор...)"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_102.png" # HERMIONE
                                        her "(Время завершающего акта!)"
                                        hide screen h_head2 
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Гермиона нагибается и ее трусики соскальзывают вниз."
                                        ">Ее движения лишены грации..."
                                        ">Но ее хорошенькая киска тем не менее вам нравится..."
                                        ">Вы показываете свое одобрение, начиная дрочить быстрее..."
                                        
                                       
                                        hide screen blktone8 
                                        hide screen blktone
                                        with d3
                                        hide screen bld1
                                        with d3
                                        show screen ctc
                                        pause
                                        $ h_c_u_pic = "no_panties_dance_ani"
                                        hide screen no_shirt_no_skirt_dance
                                        show screen h_c_u
                                        with d3
                                        pause
                                        show screen bld1
                                        with d3
                                        show screen blktone
                                        with d3
                                        
                                        $ s_sprite = "03_hp/10_snape_main/snape_18.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Да... Да!!!"
                                        sna2 "Теперь потряси этими сиськами для меня, ты, шлюха!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_99.png" # HERMIONE
                                        her "......."
                                        hide screen h_head2       
                                        hide screen ctc
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Гермиона неожиданно прерывается на серию довольно сложных пируэтов."
                                        $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Да, такая грация..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Это гибкое молодое тело!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "........."
                                        $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "О, да!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "{size=-5}(Три-два-раз... Три-два-раз... And step!){/size}"
                                        hide screen h_head2     
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Гермиона выглядит очень сосредоточенной на своем танце..."
                                        hide screen blktone8
                                        with d3
                                        $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Да, и еще один пируэт!"
                                        sna "Великолепно!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Я бы тебе поаплодировал, но одна моя рука занята."
                                        hide screen s_head2  
                                        m "{size=-4}(Это была попытка пошутить?){/size}"
                                        m "{size=-4}(Черт, возбужденный Снейп такой странный...){/size}"
                                        show screen blktone8
                                        with d3
                                        ">Гермиона начинает еще одну серию движений и пируэтов..."
                                        ">Делает реверанс воображаемой публике..."
                                        show screen blkfade
                                        with d3
                                        $ hermione_chibi_xpos = -210 #400 = Near the desk.
                                        $ hermione_chibi_ypos = 10
                                        $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                        ">И после этого измученно падает на задницу."
                                        
                                        hide screen blktone
                                        with d3
                                        hide screen blktone8
                                        with d3
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1 
                                        with d3
                                        show screen ctc
                                        pause
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_102.png"
                                        her "Фью... Это было--"
                                        hide screen h_head2
                                        with hpunch
                                        g4 "АРГХ! ТЫ ЕБАНАЯ ШЛЮХА!"
                                        #__#hide screen hermione_main
                                        #__#with d3
                                        $herView.hideQQ()
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ genie_chibi_xpos = -210
                                        $ genie_chibi_ypos = 10
                                        $ genie_cum_chibi_xpos =  -210
                                        $ genie_cum_chibi_ypos  = 10
                                        $ g_c_c_u_pic = "genie_cum_03"
                                        $ h_c_u_pic = "03_hp/08_animation_02/08_sits_02.png"
                                        show screen g_c_c_u
                                        pause
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ h_body = "03_hp/13_hermione_main/body_104.png"
                                        $ u_sperm = "03_hp/13_hermione_main/auto_04.png"
                                        show screen h_head2  
                                        her "??!!!"
                                        hide screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_97.png"
                                        show screen h_head2  
                                        
                                        $ s_sprite = "03_hp/10_snape_main/snape_18.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Хорошая работа, ты, шлюшка!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Вот твоя награда!"
                                        hide screen s_head2     
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ snape_chibi_xpos = -210
                                        $ snape_chibi_ypos = 10
                                        $ snape_cum_chibi_xpos =  -210
                                        $ snape_cum_chibi_ypos  = 10
                                        $ s_c_c_u_pic = "snape_cum_01"
                                        show screen s_c_c_u
                                        pause
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ h_body = "03_hp/13_hermione_main/body_104.png"
                                        $ u_sperm = "03_hp/13_hermione_main/auto_04.png"
                                        show screen h_head2  
                                        $ u_sperm = "03_hp/13_hermione_main/auto_05.png"
                                        her "!!!!!!!!!!!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "О... Да..."
                                        hide screen s_head2 
                                        g4 "Маленькая блядь!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "..............................."
                                
                                        $ s_c_c_u_pic = "03_hp/08_animation_02/11_cum_18.png"
                                        $ g_c_c_u_pic = "03_hp/08_animation_02/09_cum_18.png"
                                        $ s_sprite = "03_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Ха-ха-ха! Это было превосходно!"
                                        hide screen s_head2
                                        g9 "Я знаю!"
                                        show screen bld1
                                        with d3
                                        $ g_c_u_pic = "03_hp/08_animation_02/06_jerking_01.png" # Genie stands still with his dick in hand.
                                        $ s_c_u_pic = "03_hp/08_animation_02/10_jerking_01.png" # Snape stands still with his dick in hand.
                                        $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Да... Нам стоит делать это почаще..."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "................."
                                        $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Ваше выступление было неплохим, Мисс Грейнджер..."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                                        her "Спасибо................"
                                        $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Но если я здесь чтобы оценить это..."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                                        her "..........."
                                        $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Хм...."
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                                        her "............"
                                        $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "\"{size=+5}2+{/size}\"!"
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_112.png" # HERMIONE
                                        stop music
                                        her "{size=+5}ЧТО?!!!{/size}"
                                        $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Да... Думаю кое-что можно было бы и улучшить."
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_110.png" # HERMIONE
                                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                        her "Не могу поверить!"
                                        hide screen h_head2 
                                        pause
                                        show screen blkfade 
                                        with d3
                                        hide screen h_c_u 
                                        hide screen s_c_c_u
                                        hide screen g_c_c_u
                                        show screen genie
                                        $ snape_chibi_xpos = -60
                                        $ snape_chibi_ypos = 10
                                        $ s_c_u_pic = "jerking_off_03_ani" #Snape.
                                        hide screen chair_02
                                        hide screen g_c_u
                                        hide screen desk_02
                                        $ hermione_chibi_xpos = 300 #Near the desk: 400. (210 - standing on desk.)
                                        $ hermione_chibi_ypos = 260#Default: 250. (180- standing on desk.)
                                        show screen h_c_u 
                                        $ h_c_u_pic = im.Flip("03_hp/08_animation_02/07_dance_03.png", horizontal=True)
                                        ">Гермиона в ярости спрыгивает со стола."
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1
                                        with d3
                                        pause
                                        $ flip = True # Flips hermione_main screen.
                                        $ u_sperm = im.Flip("03_hp/13_hermione_main/auto_05.png", horizontal=True)
                                        $ h_body = im.Flip("03_hp/13_hermione_main/body_101.png", horizontal=True) #Sprite of Hermione's upper body.
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                                        $ only_upper = True #No legs shown.
                                        show screen bld1
                                        with d5
                                        show screen hermione_main
                                        with d3
                                        pause
                                        hide screen ctc
                                        her "Я требую более высокую оценку за это!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                                        show screen s_head2      
                                        sna2 "Не требуйте оценку Мисс Грейнджер, вы заработали ее."
                                        hide screen s_head2     
                                        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                                        $herView.hideQQ()
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = im.Flip("03_hp/13_hermione_main/body_107.png", horizontal=True) #Sprite of Hermione's upper body.                    #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "Я заслужила ее!"
                                        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                                        $herView.hideQQ()
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = im.Flip("03_hp/13_hermione_main/body_103.png", horizontal=True) #Sprite of Hermione's upper body.                    #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "И не могли бы вы хотя бы для порядочности перестать трогать себя, сэр?!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2     
                                        sna2 "Тс..."
                                        hide screen s_head2   
                                        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        #__#with d3   
                                        $herView.hideQQ()
                                        m "(Она это вправду?)"
                                        show screen ctc
                                        pause
                                        show screen blkfade
                                        with d7
                                        hide screen ctc
                                        hide screen s_c_u
                                        hide screen h_c_u
                                        $ hermione_chibi_xpos = 400 #Near the desk.
                                        $ hermione_chibi_ypos = 250 #Default: 250
                                        show screen hermione_02 #Hermione stands still.
                                        ">Вы видите как Снейп, со все еще стоящим членом и полностью покрытая спермой Гермиона громко спорят о воображаемой оценке."
                                        ">Наконец профессор Снейп соглашается изменить ее оценку с \"2+\" на \"3-\"."
                                        ">После этого он поспешно уходит, до того как Гермиона найдет еще один аргумент..."
                                        hide screen blkfade
                                        with d5
                                        $ flip = False # Flips hermione_main
                                        $ only_upper = False #Show legs.
                                        $ aftersperm = True #Show cum stains.
                                        $ uni_sperm = False #Don't show cum.
                                        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                                        $herView.hideQQ()
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ pos = POS_140
                                        #__#$ h_body = "03_hp/13_hermione_main/body_29.png"#Sprite of Hermione's upper body.                    #HERMIONE
                                        $ badges = True
                                        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                                        $herView.showQQ( "body_29.png", pos )
                                        her "Что же..."
                                        her "Наша миссия была успешной, сэр?"
                                        menu:
                                            m "..."
                                            "\"А? Какая миссия?\"":
                                                $ mad += 7
                                                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                                                $herView.hideQQ()
                                                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                                #__#$ h_body = "03_hp/13_hermione_main/body_32.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                                                $herView.showQQ( "body_32.png", pos )
                                                her "Я согласилась на это только ради того, чтобы вы увидели профессора Снейпа в действии, сэр!"
                                                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                                                $herView.hideQQ()
                                                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                                #__#$ h_body = "03_hp/13_hermione_main/body_33.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                                                $herView.showQQ( "body_33.png", pos )
                                                her "Так что у нас есть неопровержимое доказательство того, что он \"грязный\"!"
                                                m "О, эта миссия..."
                                                m "Да. Миссия выполнена!"
                                            "\"Да! Спасибо вам!\"":
                                                pass
                                        m "Хорошая работа, мисс Грейнджер."
                                        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                                        $herView.hideQQ()
                                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        #__#$ h_body = "03_hp/13_hermione_main/body_33.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                                        $herView.showQQ( "body_33.png", pos )
                                        her "Я была рада помочь, сэр!"
                                        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                                        $herView.hideQQ()
                                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        #__#$ h_body = "03_hp/13_hermione_main/body_34.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                                        $herView.showQQ( "body_34.png", pos )
                                        her "...Могу ли я теперь получить оплату?"
                                        

                                    else:
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_94.png" # HERMIONE
                                        her "О..."
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_97.png" # HERMIONE
                                        her "Нет, я не могу! Это того не стоит!"
                                        hide screen ctc
                                        hide screen h_head2  
                                        pause.1
                                        show screen blkfade
                                        with d5
                                        ">Гермиона спрыгивает со стола и начинает одеваться."
                                        $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Это ужасно разочаровывает..."
                                        hide screen s_head2  
                                        g4 "И не говори..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Пожалуй я могу вас покинуть. Поговорим позже, Альбус."
                                        hide screen s_head2  
                                        m "Да, попозже, Северус."
                                        $ s_sprite = "03_hp/10_snape_main/snape_04.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Мисс Грейнджер..."
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_99.png" # HERMIONE
                                        her "Профессор..."
                                        hide screen h_head2          
                                       # her "Я хочу получить свои очки."
                                        show screen ctc
                                        pause.4
                                        hide screen s_c_u
                                        hide screen ctc
                                        ">Профессор Снейп уходит..."
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                                        stop music fadeout 1.0
                                        her "...................."
                                        hide screen h_head2
                                        pause.5
                                        ">.................{w}.................{w}.................{w}................."
                                        show screen h_head2                                                              # HERMIONE
                                        
                                        $ badges = True # Turns badges back on.
                                        
                                        $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                                        her "...Могу ли я получить оплату... сэр...?"
                                        hide screen h_head2   

                        "- Продолжать смотреть -":
                            label civil_with_snape:
                                play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                            # JUST WATCHING.
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "Я просто продолжу танцевать..."
                            hide screen h_head2 
                            hide screen ctc
                            pause.1
                            show screen blktone8
                            with d3
                            ">Гермиона сжимает свою грудь и немного покачивает бедрами..."
                            hide screen blktone8
                            with d3
                            m "Да, девочка. Очень хорошо."
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "*Кхм!* Неплохое выступление, Мисс Грейнджер."
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "...."
                            hide screen h_head2    
                            m "Хех..."
                            m "Как вы оцените ее грудь?"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_90.png" # HERMIONE
                            her "......"
                            $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Хм......"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_90.png" # HERMIONE
                            her "........"
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "\"4+\"!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_94.png" # HERMIONE
                            her "!!!"
                            hide screen h_head2
                            m "Правда?"
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да. Я всегда отдаю должное."
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_95.png" # HERMIONE
                            her "(Профессор...)"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "(Время для завершающего акта!)"
                            hide screen h_head2   
                            pause.1
                            show screen blktone8
                            with d3
                            ">Гермиона нагибается и ее трусики соскальзывают вниз."
                            ">Ее движения лишены грации..."
                            ">Но ее хорошенькая киска тем не менее вам нравится..."
                            hide screen blktone
                            with d3
                            $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да...Да..."
                            sna2 "Теперь потряси этими сиськами для меня, шлюха!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_99.png" # HERMIONE
                            her "......."
                            hide screen h_head2       
                            show screen blktone8
                            with d3
                            ">Гермиона неожиданно прерывается на серию довольно сложных пируэтов."
                            $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да, такая грация..."
                            $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Это гибкое, молодое тело!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "{size=-5}(Три-два-раз... Три-два-раз... And step!){/size}"
                            hide screen h_head2 
                            ">HГермиона выглядит очень сосредоточенной на своем танце..."
                            $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                            show screen s_head2
                            sna "Да, и еще один пируэт!"
                            sna "Великолепно!"
                            hide screen s_head2
                            show screen blkfade
                            with d3
                            ">Гермиона начинает еще одну серию движений и пируэтов..."
                            ">Делает реверанс воображаемой публике..."
                            ">И после этого измученно падает на задницу"
                            $ hermione_chibi_xpos = -210 #400 = Near the desk.
                            $ hermione_chibi_ypos = 10
                            $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                            show screen h_c_u
                            hide screen blkfade
                            with d3
                            hide screen blktone8
                            with d3
                            $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Хорошая работа, ты шлюха!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_105.png" # HERMIONE
                            her "............."
                            if daytime:
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2                                                          #SNAPE
                                sna2 "Что ж, мой урок скоро должен начаться, поэтому я вас покину."
                                sna2 "Разве у вас нет урока зельеделия со мной сегодня, Мисс Грейнджер?"
                                show screen h_head2                                                              # HERMIONE
                                $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                                her2 "Да, сэр..."
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2                                                          #SNAPE
                                sna2 "Тогда не опаздывай, девочка..."
                                hide screen s_head2      
                            else:
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2    
                                sna2 "Что ж, уже довольно поздно. Я покину вас."
                                sna2 "Доброй ночи, Альбус."
                                hide screen s_head2    
                                m "Северус."
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2    
                                sna2 "Шлюха."
                                show screen h_head2                                                              # HERMIONE
                                $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                                her2 "Профессор..."
                                hide screen h_head2      


                            show screen ctc
                            pause
                            show screen blkfade
                            hide screen s_c_u
                            hide screen ctc
                            with d5
                            ">Профессор Снейп уходит..."
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                            stop music fadeout 1.0
                            her "...................."
                            hide screen h_head2
                            pause.5
                            ">.................{w}.................{w}.................{w}................."
                            $ badges = True
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                            her "Могу я... получить оплату... сэр...?"
                            hide screen h_head2   


                "\"Мм... Это плохая идея...\"":
                    label no_snape_watching:  
                    hide screen blktone
                    with d3
                    m "Мисс Грейнджер, как насчет еще одного стриптиза?"     
                    #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    $ pos = POS_140
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_66.png", pos )
                    her ".............."
                    her "Я скорее откажусь, профессор..."
                    m "Почему? Ты становишься довольно хороша в этом."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_79.png", pos )
                    her "........................."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_87.png", pos )
                    her "Тридцать пять очков?"
                    m "Конечно! Обычная цена."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_69.png", pos )
                    her "..................."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    hide screen bld1
                    with d3
                    pause
                    #Walks to the door
                    
                    $ walk_xpos=400 #Animation of walking chibi. (From) 400 = desk.
                    $ walk_xpos2=650 #Coordinates of it's movement. (To) 610 = door.
                    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                    show screen hermione_walk_01_f 
                    pause 2
                    hide screen hermione_walk_01_f 
                    $ hermione_chibi_xpos = 650 # Position of the chibi (Near the door).
                    $ h_c_u_pic = im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
                    show screen h_c_u
                    pause.5
                   
                    $ tt_xpos=670
                    $ tt_ypos=200
                    show screen thought 
                    with Dissolve(.3)
                    pause.5
                    hide screen thought
                    pause.5
                   
                    $ h_c_u_pic = im.Flip("03_hp/animation/h_walk_03.png", horizontal=True)
                    $ renpy.play('sounds/09_lock.wav') #Sound of a door opening.
                    pause.4
                    $ h_c_u_pic = im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
                    show screen ctc
                    pause
                    m "??!"
                    hide screen h_c_u
                    hide screen ctc
                    $ walk_xpos=650 #Animation of walking chibi. (From)
                    $ walk_xpos2=400 #Coordinates of it's movement. (To)
                    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                    show screen hermione_walk_01 
                    pause 3
                    $ hermione_chibi_xpos = 400 #Near the desk.
                    show screen hermione_02 #Hermione stands still.
                    show screen bld1
                    with Dissolve(.3)
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    $ h_ypos=0
                    $ pos = POS_140
                    #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_69.png", pos )
                    her "Просто на всякий случай..."
                    stop music fadeout 1.0
                    #__#hide screen hermione_main
                    $herView.hideQ() #"WARNING_Z"
                    with d5

                    show screen blkfade
                    with Dissolve(1)
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 5
                    $ h_body = "03_hp/13_hermione_main/body_16.png"
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    show screen h_head2
                    her2 "Просто для протокола..."
                    $ h_body = "03_hp/13_hermione_main/body_17.png"
                    her2 "Я все еще считаю, что это совершенно недопустимая услуга, покупать одну из своих студенток, сэр."
                    hide screen h_head2
                    m "Правильно. И уж более неуместно продавать себя своему директору. Не согласишься?"
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_69.png"
                    her ".........."
                    hide screen h_head2
                    hide screen blkfade
                    hide screen bld1
                    $ hermione_chibi_xpos = 210 #Near the desk: 400.
                    $ hermione_chibi_ypos = 180 #Default: 250
                    show screen clothed_dance #Hermione stands still.
                    show screen ctc
                    with fade
                    pause
                    show screen no_vest_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_87.png"
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her ".............."
                    $ h_body = "03_hp/13_hermione_main/body_85.png"
                    her2 "Что если мои родители узнают об этом, сэр?"
                    her2 "Мама никогда не поймет..."
                    $ h_body = "03_hp/13_hermione_main/body_44.png"
                    her "А насчет моего отца..."
                    hide screen h_head2
                    menu:
                        m "..."
                        "{size=-3}\"Твой отец гордился бы тобой!\"{/size}":
                            show screen h_head2
                            her "Я сомневаюсь..."
                            her "Да, я делаю это в благих целях, но..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_61.png"
                            her "Он никогда не видел меня такой..."
                            her "Он никогда не должен узнать об этом..."
                            hide screen h_head2
                        "{size=-3}\"Твой папочка отшлепал бы тебя!\"{/size}":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_48.png"
                            her "Он бы не посмел!"
                            $ h_body = "03_hp/13_hermione_main/body_44.png"
                            her "И в любом случае я уже взрослая для такого..."
                            hide screen h_head2
                            g9 "Я бы сказал, что ты в идеальном возрасте для такого..."
                            show screen h_head2
                            her "А?"
                            $ h_body = "03_hp/13_hermione_main/body_57.png"
                            her "Я не понимаю о чем вы, сэр."
                            hide screen h_head2
                        "{size=-3}\"Твой папочка отрекся бы от тебя!\"{/size}":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_34.png"
                            her "Вы вероятно правы, сэр..."
                            $ h_body = "03_hp/13_hermione_main/body_22.png"
                            her "(Ох папочка, мне очень жаль...)"
                            $ h_body = "03_hp/13_hermione_main/body_21.png"
                            her "Он никогда не должен узнать..."
                            hide screen h_head2
                        "{size=-3}\"Твой отец хотел бы посмотреть на это!\"{/size}":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_33.png"
                            her "Он бы не посмел! Ему было бы стыдно за меня!"
                            hide screen h_head2
                            m "Ты в этом уверена?"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_32.png"
                            her "Абсолютно! Мой папа культурный человек!"
                            hide screen h_head2
                            m "Но {size=+4}он{/size} {size=+4}мужчина{/size}, верно?"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_50.png"
                            her "....................."
                            $ h_body = "03_hp/13_hermione_main/body_29.png"
                            her "Папа никога не должен узнать об этом..."
                            hide screen h_head2
                    show screen blktone
                    with d3
                    ">Гермиона начнает соблазнительно качать бедрами, пока ее юбка соскальзывает с ее тела..."
                    hide screen blktone
                    with d3
                    hide screen bld1
                    with d3
                    show screen ctc
                    pause
                    show screen no_skirt_dance
                    with d3
                    pause
                    hide screen ctc
                    show screen bld1
                    with d3
                    
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_31.png"
                    her "Профессор?"
                    hide screen h_head2
                    m "А?"
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_44.png"
                    her "Могу я задать вопрос?"
                    hide screen h_head2
                    m "Попробуй..."
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_33.png"
                    her "..............."
                    $ h_body = "03_hp/13_hermione_main/body_57.png"
                    her "Вы когда-нибудь любили...?"
                    hide screen h_head2
                    menu:
                        m "..."
                        "\"Это смешно! Любовь это ложь!\"":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_29.png"
                            her "Очень жаль, что вы так считаете, сэр!"
                            $ h_body = "03_hp/13_hermione_main/body_50.png"
                            her "Но вы можете очень сильно ошибаться!"
                            $ h_body = "03_hp/13_hermione_main/body_54.png"
                            her2 "Я считаю, что настоящая любовь вращает Землю!"
                            hide screen h_head2
                            m "На самом деле момент сохранения импульса отвечает за это."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_44.png"
                            her "А?"
                            hide screen h_head2
                            m "Забудь. Готова снять рубашку?"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_50.png"
                            her "............"      
                            hide screen h_head2
                        "\"Молчи и продолжай танцевать\"":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_50.png"
                            her "Но вы сказали, что я могла задать вопрос..."
                            hide screen h_head2
                            m "И ты это сделала, не так ли?"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_31.png"
                            her "!!!............"
                            $ h_body = "03_hp/13_hermione_main/body_50.png"
                            her2 "...................................."
                            hide screen h_head2
                            m "Теперь снимай свою рубашку."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_69.png"
                            her "........"
                            hide screen h_head2
                        "\"Да...очень и очень давно...\"":
                            hide screen h_head2
                            m "Да... очень и очень давно..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_31.png"
                            her2 "!!!!!??.............................."
                            hide screen h_head2
                            m "Ее имя было Эден..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_45.png"
                            her "Она была красива?"
                            hide screen h_head2
                            m "Более чем..."
                            m "Она была умна, зелена и совершенна..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_87.png"
                            her "Она была... \"зелена\"...?"
                            $ h_body = "03_hp/13_hermione_main/body_47.png"
                            her2 "Вы издеваетесь, сэр?"
                            hide screen h_head2
                            m "Ох, вы люди, ничего не знаете о настоящей любви..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_55.png"
                            her ".....................................?"
                            hide screen h_head2
                            m "Э-э...то есть, снимай рубашку, девочка!"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_69.png"
                            her "................."
                            hide screen h_head2
                        "\"Мне кажется я влюбляюсь прямо сейчас!\"":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_69.png"
                            her "Не нужно быть таким вульгарным, сэр."
                            hide screen h_head2
                            m "Ох, но мне кажется это так!"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_66.png"
                            her "Сэр, Пожалуйста!"
                            $ h_body = "03_hp/13_hermione_main/body_55.png"
                            her "Я одна из ваших студенток!"
                            $ h_body = "03_hp/13_hermione_main/body_57.png"
                            her "И вы старе моего отца!"
                            hide screen h_head2
                            m "{size=-4}(Не представляешь насколько, девочка.){/size}"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_55.png"
                            her2 "Некоторые ученые считают, что \"любовь\" это ничто иное, как химическая реакция..."
                            $ h_body = "03_hp/13_hermione_main/body_16.png"
                            her2 "И когда человек испытывает сексуальное влечение, тот же тип гормонов--"
                            hide screen h_head2
                            m "Мисс Грейнджер!"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_15.png"
                            her "Да, сэр?"
                            hide screen h_head2
                            m "Вы забыли чем мы занимаемся?"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_24.png"
                            her "Ох, мои извинения, сэр... Иногда я отвлекаюсь."
                            hide screen h_head2
                            m "Давай ты уже снимешь свою рубашку?!"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_29.png"
                            her "Верно..."
                            hide screen h_head2
                    show screen blktone
                    with d3
                    ">Гермиона расстегивает последнюю пуговицу на рубашке и изящно скидывает ее..."
                    hide screen blktone
                    with d3
                    hide screen bld1
                    with d3
                    show screen ctc
                    pause
                    show screen no_shirt_no_skirt_dance
                    with d3
                    pause
                    hide screen ctc
                    show screen bld1
                    with d3
                    g9 "Да! Сисьски!"
                    
                    $ badges = False # Hides any badges from hermione_main screen.
                    
                    show screen h_head2
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    $ h_body = "03_hp/13_hermione_main/body_90.png"
                    her "Вам обязательно быть настолько пошлым, сэр?"
                    hide screen h_head2
                    menu: 
                        "- Достать член и начать дрочить -":
                            hide screen bld1
                            show screen ctc
                            with d3
                            pause
                            show screen blkfade
                            with d6
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_94.png"
                            her "Профессор Дамблдор?!"
                            hide screen h_head2
                            m "Все в порядке, девочка. Доверься мне..."
                            
                            
                            hide screen genie
                            hide screen no_shirt_no_skirt_dance
                            $ genie_chibi_xpos = -185
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "jerking_off_02_ani"
                            show screen chair_02
                            show screen g_c_u
                            show screen desk_02
                            show screen no_shirt_no_skirt_dance
                            hide screen blkfade
                            with fade
                            pause
                            show screen bld1
                            with d3
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_95.png"
                            her "Н-но..."
                            her "Ваш..."
                            hide screen h_head2
                            m "Да... Ах, да, это великолепно..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_98.png"
                            her "Профессор!!!"
                            her "Я хочу, чтобы вы убрали эту..."
                            $ h_body = "03_hp/13_hermione_main/body_99.png"
                            her "...штуку."
                            hide screen h_head2
                            menu:
                                m "..."
                                "\"Я сказал, продолжай танцевать, девочка!\"":
                                    if whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_99.png"
                                        her "Но..."
                                        her "............................."
                                        $ h_body = "03_hp/13_hermione_main/body_101.png"
                                        her2 "Ну, ладно, но если только вы пообешаете мне на кончать, сэр."
                                        hide screen h_head2
                                        menu:
                                            m "..."
                                            "- Пообещать сдержаться -":
                                                    $ d_flag_07 = True #Promised to hold it.
                                                    show screen h_head2
                                                    $ h_body = "03_hp/13_hermione_main/body_102.png"
                                                    her "Ну, тогда ладно..."
                                                    hide screen h_head2
                                            "- Не давать такого обещания -":
                                                $ d_flag_07 = False #Did not promise to hold it.
                                                m "\"Не кончать\"? Это похоже на пытку!"
                                                m "Пожалуйста, сдержите свои садистские наклонности, Мисс Грейнджер."
                                                show screen h_head2
                                                $ h_body = "03_hp/13_hermione_main/body_103.png"
                                                her "У меня нет никаких... садистких наклонностей, сэр!"
                                                her "Я просто хочу, чтобы..."
                                                hide screen h_head2
                                                g9 "Да... У тебя такие отличные сиськи..."
                                                show screen h_head2
                                                $ h_body = "03_hp/13_hermione_main/body_97.png"
                                                her "............"
                                                hide screen h_head2
                                                g9 "А-ах... Да..."
                                                show screen h_head2
                                                $ h_body = "03_hp/13_hermione_main/body_97.png"
                                                her ".........."
                                                $ h_body = "03_hp/13_hermione_main/body_99.png"
                                                her "Ладно! Будь по вашему, сэр!"
                                                $ h_body = "03_hp/13_hermione_main/body_103.png"
                                                her "{size=-5}(Как обычно...){/size}"
                                                hide screen h_head2
                                        show screen blktone
                                        with d3
                                        ">Вы продолжаете дрочить, наблюдая за Гермионой..."
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_90.png"
                                        her "Время кончить, я пологаю..."
                                        hide screen h_head2
                                        m "Да, девочка! Снимай свои трусики!"
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_91.png"
                                        her "........"
                                        hide screen h_head2
                                        show screen blktone8
                                        with d3
                                        ">Гермиона слегка наклоняется и стягивает с себя трусики..."
                                        ">Вы видите, что она делает все возможное, чтобы это выглядело изящно..."
                                        ">Но ее попытки выглядеть как настоящая стриптизерша, выглядят довольно смешно..."
                                        hide screen blktone8 
                                        hide screen blktone
                                        with d3
                                        hide screen bld1
                                        with d3
                                        pause
                                        $ h_c_u_pic = "no_panties_dance_ani"
                                        hide screen no_shirt_no_skirt_dance
                                        show screen h_c_u
                                        with d3
                                        pause
                                        show screen bld1
                                        with d3
                                        show screen blktone
                                        with d3
                                        ">Тем не менее вы показываете ей, что у нее получается весьма неплохо..."
                                        ">Начиная дрочить еще быстрее!"
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_91.png"
                                        her ".........."
                                        hide screen h_head2
                                        show screen blktone8
                                        with d3
                                        ">Внезапно Гермиона начинает выдавать целые сложные пируэты..."
                                        m "{size=-4}(Это выглядит очень даже не дурно...){/size}"
                                        ">Гермиона хватает и слегка скручивает свои сиськи, после чего снова делает серию сложны пируэтов (иногда нелепых)..."
                                        m "{size=-4}(Она практиковалась?){/size}"
                                        g9 "Ох, какое мне дело?"
                                        ">Вы начинаете еще сильнее надрачивать ваш твердый как алмаз член."
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_102.png"
                                        her "{size=-5}(Три-два-раз... Три-два-раз... И шаг!){/size}"
                                        hide screen h_head2
                                        ">Гермиона выполняет другую партию движений, которые выглядет весьма стильно..."
                                        ">Ее упругие сиськи подпрыгивают в такт танцу..."
                                        g9 "Да, да, маленькая шлюха!"
                                        ">Еще несколько движений, пара жестов и небольшой реверанс-поклон воображаемой публике..."
                                        show screen blkfade
                                        with d3
                                        $ hermione_chibi_xpos = -210 #400 = Near the desk.
                                        $ hermione_chibi_ypos = 10
                                        $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                        ">И под конец она падает на свою попку."
                                        hide screen blktone
                                        with d3
                                        hide screen blktone8
                                        with d3
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1 
                                        with d3
                                        pause
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_102.png"
                                        her "Фиу... Это было--"
                                        hide screen h_head2
                                        with hpunch
                                        g4 "АРГХ! ЕБАНАЯ ДЫРКА!"
                                        #__#hide screen hermione_main
                                        #__#with d3
                                        $herView.hideQQ()
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ genie_chibi_xpos = -210
                                        $ genie_chibi_ypos = 10
                                        $ genie_cum_chibi_xpos =  -210
                                        $ genie_cum_chibi_ypos  = 10
                                        $ g_c_c_u_pic = "genie_cum_03"
                                        $ h_c_u_pic = "03_hp/08_animation_02/08_sits_02.png"
                                        show screen g_c_c_u
                                        pause
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ h_body = "03_hp/13_hermione_main/body_104.png"
                                        $ u_sperm = "03_hp/13_hermione_main/auto_04.png"
                                        show screen h_head2  
                                        her "??!!!"
                                        hide screen h_head2
                                        show screen bld1
                                        with d3
                                        $ h_body = "03_hp/13_hermione_main/body_97.png"
                                        show screen h_head2  
                                        her "Профессор!!!"
                                        $ g_c_c_u_pic = "03_hp/08_animation_02/09_cum_18.png"
                                        hide screen h_head2
                                        if d_flag_07: #Promised to hold it.
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "03_hp/13_hermione_main/body_97.png" # HERMIONE
                                            her "Нет, профессор! Вы обещали!"
                                            hide screen h_head2
                                            g4 "Ох, детка... Это было довольно круто..."
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "03_hp/13_hermione_main/body_98.png" # HERMIONE
                                            her "ВЫ не сдержали слово, сэр!"
                                            hide screen h_head2
                                            m "А? О чем ты говоришь?"
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "03_hp/13_hermione_main/body_113.png" # HERMIONE
                                            her "Как вы могли так со мной поступить, сэр?"
                                            hide screen h_head2
                                            m "Ох, успокойся, девочка."
                                            m "Сегодня ты заслужила свои очки."
                                            m "Теперь, просто оденься и уходи, пока кто-нибудь не застукал нас тут."
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "03_hp/13_hermione_main/body_114.png" # HERMIONE
                                            her "*всхлип!*........................"
                                            hide screen h_head2        
                                            $ mad += 50
                                            show screen blkfade 
                                            with d3
                                            $ uni_sperm = False #Sperm layer is not displayed.
                                            $ aftersperm = True #Aftersperm layer is displayed. 
                                            stop music fadeout 5.0
                                            ">.................{w}.................{w}.................{w}................."
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "03_hp/13_hermione_main/body_12.png" # HERMIONE
                                            her "...Могу я получить оплату, сэр... пожалуйста?"
                                            hide screen h_head2   
                                            jump done_with_dancing
                                        else:
                                            $ h_body = "03_hp/13_hermione_main/body_97.png"
                                            show screen h_head2  
                                            her "Было жарко..."
                                            hide screen h_head2  
                                            $ g_c_u_pic = "03_hp/08_animation_02/06_jerking_01.png" # Genie stands still with his dick in hand.
                                            m "Аха... Даа... Это просто безумие..."
                                            $ h_body = "03_hp/13_hermione_main/body_105.png"
                                            show screen h_head2  
                                            her "Вы всю меня обкончали..."
                                            her "Я вам ученик и ..."
                                            $ h_body = "03_hp/13_hermione_main/body_106.png"
                                            show screen h_head2  
                                            her "Вы просто кончили на меня..."
                                            hide screen h_head2  
                                            g9 "Я знаю! Довольно круто, да?!"
                                            $ h_body = "03_hp/13_hermione_main/body_107.png"
                                            show screen h_head2  
                                            her "Ничего подобного!"
                                            #her "You should not have done this, сэр!"
                                            her2 "Вы должны вести себя как подобает директору!"
                                            hide screen h_head2  
                                            m "Правда? Что ты хочешь от меня?"
                                            m "Направить его в сторону стены или обратно в трусы и просто кончить?"
                                            $ h_body = "03_hp/13_hermione_main/body_105.png"
                                            show screen h_head2
                                            her "........"
                                            $ h_body = "03_hp/13_hermione_main/body_101.png"
                                            show screen h_head2
                                            her "Тем не менее, вы не должны были..."
                                            $ h_body = "03_hp/13_hermione_main/body_102.png"
                                            show screen h_head2
                                            her "Я согласилась танцевать для вас..."
                                            her "Но я не соглашалась быть оскверненной вашей спермой."
                                            hide screen h_head2  
                                            m "Я думаю, это уже произошло..."
                                            $ h_body = "03_hp/13_hermione_main/body_100.png"
                                            show screen h_head2
                                            her "Я требую дополнительные очки за это!"
                                            hide screen h_head2  
                                            m "Конечно, как иначе..."
                                            menu:
                                                m "..."
                                                "\"Ты получишь 1 дополнительное очко.\"":
                                                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                                    $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                    show screen h_head2
                                                    her "Одно дополнительное очко?"
                                                    $ h_body = "03_hp/13_hermione_main/body_98.png"
                                                    her2 "Одно жалкое очко за все, что вы со мной сделали?"
                                                    $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                    her "Это просто оскорбительно, сэр!"
                                                    hide screen h_head2  
                                                    m "Одно очко, Мисс Грейнджер. Забирайте или уходите."
                                                    $ h_body = "03_hp/13_hermione_main/body_103.png"
                                                    show screen h_head2
                                                    her "............."
                                                    $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                    her "Я беру его."
                                                    hide screen h_head2  
                                                    $ mad += 30
                                                    $ current_payout = 36
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"Десять дополнительных очков.\"":
                                                    $ current_payout = 45
                                                    $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                    show screen h_head2
                                                    her "Десять дополнительных очков, сэр?"
                                                    her "Но это слишком мало!"
                                                    hide screen h_head2  
                                                    m "Десять очков. Берите или уходите, Мисс Грейнджер."
                                                    $ h_body = "03_hp/13_hermione_main/body_103.png"
                                                    show screen h_head2
                                                    her "..............."
                                                    $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                    show screen h_head2
                                                    her "Ну, ладно... Лучше чем ничего..."
                                                    hide screen h_head2  
                                                    $ mad += 11
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"Вы получите 25 дополнительных очков.\"":
                                                    $ current_payout = 60
                                                    $ h_body = "03_hp/13_hermione_main/body_102.png"
                                                    show screen h_head2
                                                    her2 "Да, думаю этого хватит."
                                                    hide screen h_head2  
                                                    m "Теперь вы счастливы?"
                                                    $ h_body = "03_hp/13_hermione_main/body_102.png"
                                                    show screen h_head2
                                                    her "Да, сэр. Спасибо сэр."
                                                    hide screen h_head2  
                                                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"Вы получаете 50 дополнительных очков.\"":
                                                    $ current_payout = 85
                                                    $ h_body = "03_hp/13_hermione_main/body_95.png"
                                                    show screen h_head2
                                                    her "Серьезно?!"
                                                    $ h_body = "03_hp/13_hermione_main/body_94.png"
                                                    her "Ох, не знаю что сказать..."
                                                    hide screen h_head2  
                                                    m "Мне понравилось,Мисс Грейнджер."
                                                    show screen h_head2
                                                    $ h_body = "03_hp/13_hermione_main/body_109.png"
                                                    her "Спасибо сэр..."
                                                    hide screen h_head2  
                                                    m "Так же мне понравилось заливать твое гибкое тельце своей спермой..."
                                                    $ h_body = "03_hp/13_hermione_main/body_108.png"
                                                    show screen h_head2
                                                    her "Сэр......"
                                                    hide screen h_head2  
                                                    m "И так, просто позвольте мне показать свою признательность."
                                                    m "Пятьдесяц очков, заслуженно, Мисс Грейнджер."
                                                    $ h_body = "03_hp/13_hermione_main/body_108.png"
                                                    show screen h_head2
                                                    her "Огромное спасибо, сэр."
                                                    hide screen h_head2  
                                                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"Ты ни черта не получишь!\"":
                                                    stop music fadeout 1.0
                                                    $ h_body = "03_hp/13_hermione_main/body_104.png"
                                                    show screen h_head2
                                                    her "Что? Даже обычной платы?"
                                                    hide screen h_head2  
                                                    menu:
                                                        m "..."
                                                        "\"Ох, нет, их ты поучишь.\"":
                                                            $ mad += 30
                                                            $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                            show screen h_head2
                                                            her "Как великодушно с вашей стороны, сэр." 
                                                            hide screen h_head2  
                                                            hide screen bld1
                                                            with d3
                                                            pause
                                                            show screen blkfade
                                                            with d7
                                                            pause.5
                                                            $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                            jump done_with_dancing
                                                        "\"Нет, их тоже не получишь!\"":
                                                            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                                            $ h_body = "03_hp/13_hermione_main/body_104.png"
                                                            show screen h_head2
                                                            her "!!!?"
                                                            her "Я танцевала для вас, сэр..."
                                                            $ h_body = "03_hp/13_hermione_main/body_105.png"
                                                            her "Я унижалась для вашего веселья..."
                                                            $ h_body = "03_hp/13_hermione_main/body_107.png"
                                                            her "Позволила кончить на себя..."
                                                            $ h_body = "03_hp/13_hermione_main/body_110.png"
                                                            with hpunch
                                                            her "И не получу ничего?!"
                                                            hide screen h_head2  
                                                            m "Вы провалились, Мисс Грейнджер!"
                                                            $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                            show screen h_head2
                                                            her "Ох, это низко даже для вас, сэр!"
                                                            hide screen h_head2  
                                                            m "Я сказал: вы провалились."
                                                            $ h_body = "03_hp/13_hermione_main/body_110.png"
                                                            show screen h_head2
                                                            her "*Тяжелый вздох!*"
                                                            $ mad += 90
                                                            hide screen h_head2  
                                                            hide screen bld1
                                                            with d3
                                                            pause
                                                            show screen blkfade
                                                            with d7
                                                            pause.5
                                                            hide screen h_c_u
                                                            hide screen g_c_u
                                                            hide screen g_c_c_u # Genie's sperm. Universal.
                                                            hide screen ctc
                                                            hide screen chair_02
                                                            hide screen desk_02
                                                            show screen genie
                                                            show screen bld1
                                                            $ hermione_chibi_xpos = 400 #Near the desk.
                                                            $ hermione_chibi_ypos = 250 #Default: 250
                                                            show screen hermione_02 #Hermione stands still.
                                                            pause.1
                                                            hide screen blkfade
                                                            with d3
                                                            call music_block
                                                            jump could_not_flirt #Leaves without getting any очков.
                                                        

                                    else: # You jerk off your cock and Hermione is NOT OK with it.
                                        $ h_body = "03_hp/13_hermione_main/body_103.png"
                                        show screen h_head2
                                        stop music fadeout 1.0
                                        her "Нет, сэр!"
                                        hide screen h_head2  
                                        m "А?"
                                        show screen blkfade
                                        with d7
                                        ">Гермиона спрыгивает со стола и начинает спешно одеваться, посматривая на вас..."
                                        m "Ох, да ладно! Не оставляй меня так!"
                                        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                                        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                                        $ h_body = "03_hp/13_hermione_main/body_101.png"
                                        show screen h_head2
                                        her "Танец окончен, сэр!"
                                        hide screen h_head2
                                        pause 1
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_79.png"
                                        her "Я хотела бы получить очки!"
                                        hide screen h_head2
                                        m "Упрямая девчонка..."
                                        ">Вы неохотно убрали свой член..."
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_79.png"
                                        her "Полагаю, я могу получить сейчас свою оплату."
                                        hide screen h_head2
                                        jump done_with_dancing
                                "\"Ладно. Не драматизируй ты так!\"": 
                                    $ h_body = "03_hp/13_hermione_main/body_103.png"
                                    show screen h_head2
                                    her2 "......................"
                                    hide screen h_head2
                                    pause.1
                                    hide screen no_shirt_no_skirt_dance
                                    show screen genie
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk_02
                                    show screen no_shirt_no_skirt_dance
                                    hide screen blkfade
                                    with fade
                                    pause
                                    show screen bld1
                                    with d3
                                    pass

                        "- Показать хорошие манеры и просто смотреть -":
                            pass
                    # JUST WATCHING.
                    show screen blktone
                    with d3
                    ">Вы смотрите танец Гермионы..."
                    $ h_body = "03_hp/13_hermione_main/body_97.png"
                    show screen h_head2
                    her "(Время заканчивать, я полагаю...)"
                    hide screen h_head2
                    m "Да! Снимай их!"
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_90.png"
                    her "........"
                    hide screen h_head2
                    show screen blktone8
                    with d3
                    ">Гермиона нагинается и стягивает свои трусики..."
                    ">Она делает все возможное, чтобы это выглядело изящно..."
                    ">Но ее попытки выглядеть как настоящая стриптизерша выглядят довольно смешно..."
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_109.png"
                    her ".........."
                    hide screen h_head2
                    ">Внезапно она начинает выдавать целые пируэты..."
                    hide screen h_head2
                    m "{size=-4}(Это выглядит довольно неплохо...){/size}"
                    ">Гермиона хватает и слегка скручивает свои сиськи, после чего снова делает серию сложны пируэтов (иногда нелепых)..."
                    m "{size=-4}(Она практиковалась?){/size}"
                    g9 "Ох, какое мне дело?"
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_102.png"
                    her "{size=-5}(Три-два-раз... Три-два-раз... And step!){/size}"
                    hide screen h_head2
                    ">Гермиона выполняет довольно сложные движения, которые могли бы выглядет довольно стильно и круто, если бы не ее прыгающие в разные стороны сиськи..."
                    g9 "Да, да, маленькая потаскушка!"
                    
                    show screen blkfade
                    with d3
                    $ hermione_chibi_xpos = -210 #400 = Near the desk.
                    $ hermione_chibi_ypos = 10
                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                    ">Еще несколько движений, пара жестов, поклон воображаемой аудитории и Гермиона резко падает на мягкую, замучанную попку."
                    show screen h_c_u
                    hide screen blktone
                    with d3
                    hide screen blktone8
                    with d3
                    hide screen blkfade
                    with d3
                    hide screen bld1 
                    with d3
                    pause
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_108.png"
                    show screen bld1
                    with d3
                    her "Фиу... Было весьма захватывающе..."
                    hide screen h_head2 
                    menu:
                        m "..."
                        "{size=-3}\"Отличная работа, девочка! Ты правда знаешь как это делается!\"{/size}":
                            m "Отличная работа, девочка!"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_109.png"
                            her "Правда?"
                            hide screen h_head2
                            m "Да! У тебя есть талант!"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_108.png"
                            her "Спасибо сэр."
                            hide screen h_head2
                        "{size=-3}\"Хм... Это было ужасно...\"{/size}":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_105.png"
                            her "Ох... Мне жаль..."
                            hide screen h_head2
                            m "Ничего... Тебе просто нужно практиковаться..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_107.png"
                            her "Эм... Буду иметь в виду, сэр..."
                            hide screen h_head2
                        "{size=-3}\".................................................\"{/size}":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_108.png"
                            her "......................."
                            hide screen h_head2

                    
                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                    hide screen bld1
                    show screen ctc
                    with d3
                    pause
                    show screen blkfade
                    with d7
                    pause.5

                            
        else: #Stripping only for Genie.
            jump no_snape_watching 

        
        
        
    label done_with_dancing:
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3
    
    $ badges = True # Shows any badges from hermione_main screen.
    
    m "Да, Мисс Грейнджер. [current_payout] очков \"Гриффиндору\"." 
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ pos = POS_140
    #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
    #__#show screen hermione_main
    $herView.showQ( "body_13.png", pos ) #"WARNING_Z"
    hide screen hermione_01_f #Hermione stands still.
    with d3
    
    her "Спасибо, сэр..."

    if whoring <= 11:
        $ whoring +=1

    $ request_11_points += 1
    

    $ sperm_on_tits = False
    $ uni_sperm = False


    hide screen bld1
    #__#hide screen hermione_main
    $herView.hideQ() #"WARNING_Z"
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    $ aftersperm = False #Show cum stains on Hermione's uniform.
    call music_block
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu       