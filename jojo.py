import streamlit as st
import random
import time
import datetime
import pandas as pd
# import streamlit.components.v1 as stc


def main():
    st.set_page_config(page_title="Jomikuji", page_icon=':bar_chart:')

    if 'count' not in st.session_state: 
        st.session_state.count = 0 #countがsession_stateに追加されていない場合，0で初期化
    if 'key_1' not in st.session_state: 
        st.session_state.key_1 = ""
    if 'key_2' not in st.session_state: 
        st.session_state.key_2 = ""
    if 'key_3' not in st.session_state: 
        st.session_state.key_3 = ""

    st.header("2024年 新年のJomikuji")
    st.markdown("---")
    #結果(result)をリスト化
    result = [
    {'word':'酒！飲まずにはいられないッ！','attention':'酒に頼りすぎていませんか？飲む以外に出来ることをやりましょう。', 'class':'凶', 'pict':'image/sake.jpg'},
    {'word':'「根を掘る」ってのはわかる。根っこは土の中に埋まっとるからな。だが「葉掘り」って部分はどういうことだあぁぁ〜！？¥n葉っぱが掘れるかっつーのよ〜ッ！？','attention':'細かいことを気にしすぎです。広い心を持ちましょう。', 'class':'凶', 'pict':'image/giacho.JPG'},
    {'word':'わかったよ。プロシュート兄ィ！！兄貴の覚悟が！「言葉」ではなく「心」で理解できた！','attention':'今まで分からなかったことがわかるようになるはずです。', 'class':'大吉', 'pict':'image/pesshi.jpg'},
    {'word':'落ち着け、落ち着くんだ・・・「素数」を数えて落ち着くんだ・・２・・・３、５、７、１１・・・','attention':'素数を数えて、落ち着きましょう。', 'class':'吉', 'pict':'image/puchi.JPG'},
    {'word':'ねーちゃん！あしたっていまさッ！','attention':'中々始められなかったことありませんか？いまがチャンスです', 'class':'大吉', 'pict':'image/poko.jpg'},
    # {'word':'「魂」を！賭けよう！グッド','attention':'大切な決断をする時です。よく考えて決めましょう。', 'class':'吉'},
    {'word':'おれは人間をやめるぞ！ジョジョーーーッ！！','attention':'あなたは今、危険な賭けをしていませんか？思い止まりましょう。', 'class':'大凶', 'pict':'image/ishikamen.jpg'},
    {'word':'勝ったッ！第3部完！','attention':'終わったと思っていること、まだ終わっていないかもしれません。もう一度確認しましょう。', 'class':'凶', 'pict':'image/sanbukan.jpg'},
    {'word':'ホハハハフフフフヘハハハハフホホアハハハ  フハハックックックッヒヒヒヒヒケケケケケ  ノォホホノォホ','attention':'あなたがずっと困っていた事、打開策に気付き、きっと解決できるでしょう。', 'class':'大吉', 'pict':'image/kakyoin.jpg'},
    {'word':'ぬァァァめるよォオオオオにィィィィ','attention':'熱中しすぎて、周りがよく見えていないかもしれません。一度、冷静になりましょう。', 'class':'小吉', 'pict':'image/enya.jpg'},
    {'word':'あ・・・ありのまま　今起こった事を話すぜ！『おれは　奴の前で階段を登っていたと思ったら　いつのまにか降りていた』','attention':'あなたは、今発生している出来事に大変混乱しています。一度立ち止まって、冷静に考えてみましょう。','class':'吉', 'pict':'image/poruporu.jpg'},
    {'word':'『山を登る時　ルートもわからん！頂上がどこにあるかもわからんでは遭難は確実なんじゃ！』確実！そうコーラを飲んだらゲップが出るっていうくらい確実じゃッ！','attention':'あなたは目標を見失っています。立ち止まって、目標を再確認しましょう。', 'class':'吉', 'pict':'image/cora.jpg'},
    {'word':'君がッ　泣くまで　殴るのをやめないッ！','attention':'あなたはイライラしていませんか？やり過ぎには気をつけましょう。', 'class':'吉', 'pict':'image/naguru.jpg'}]

    display = [
        {'disp':'スピードワゴンはクールに占うぜ',
         'disp':'オラオラオラオラッ',
         'disp':'無駄無駄無駄無駄ッ!'}]

    name = random.choice(display)


    button = st.sidebar.button('ボタンを押すんじゃ〜〜〜ッ！')
    
    if button:
        st.session_state.count += 1 #値の更新

        dt_now = datetime.datetime.now()
        dt_now_str = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
        l = [dt_now_str]
        df_tmp = pd.DataFrame(l)
        df_tmp = df_tmp.rename(columns={0:'時刻'})
        df = pd.read_csv('frequency.csv', encoding='utf_8_sig')
        df_out1 = pd.concat([df, df_tmp], axis=0)
        df_out1.to_csv('frequency.csv', encoding='utf_8_sig', index=False)
        df_out1

        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
        #resultからランダムに選ぶ
        omikuji = random.choice(result)

        # my_bar.progress(0)
        st.balloons()
        

        st.session_state.key_1 = omikuji['word']
        st.session_state.key_2 = omikuji['class']
        st.session_state.key_3 = omikuji['pict']

        st.markdown("# "+st.session_state.key_1)
        st.markdown("## "+st.session_state.key_2)
        st.image(st.session_state.key_3)

        # st.markdown("# "+omikuji['word'])
        # st.markdown("## "+omikuji['class'])
        # st.image(omikuji['pict'])

        # stc.html("<p style='font-size: 50pt;, color: #ff0000;, font-family:MS Pゴシック,sans-serif;'>" + omikuji['word'])
        st.markdown(omikuji['attention'])
    elif st.session_state.count > 0:
        st.markdown("# "+st.session_state.key_1)
        st.markdown("## "+st.session_state.key_2)
        st.image(st.session_state.key_3)
        


    if st.session_state.count>10:
        st.markdown(str(st.session_state.count)+"回実行しています"
                    """
                    大分気に入ってもらえたようですね！
                    """)

    if st.session_state.count>0:
        st.sidebar.markdown("""
                    ---
                    """)
        # with st.sidebar.expander("もしよかったら「いいね」、もしくは「感想・ご意見」をください。"):        
        if st.sidebar.button("イイねッ！"):
            dt_now = datetime.datetime.now()
            dt_now_str = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
            l = [dt_now_str]
            df_tmp = pd.DataFrame(l)
            df_tmp = df_tmp.rename(columns={0:'時刻'})
            df2 = pd.read_csv('iine.csv', encoding='utf_8_sig')
            df_out2 = pd.concat([df, df_tmp], axis=0)
            df_out2.to_csv('iine.csv', encoding='utf_8_sig', index=False)
            df_out2
            st.sidebar.success("イイねありがとうございます！")

        with st.sidebar.form("感想・ご意見"):
            st.sidebar.text("感想・ご意見欄")
            input_name = st.sidebar.text_input("氏名")
            input_imp = st.sidebar.text_area("感想")

            # Every form must have a submit button.
            submitted = st.form_submit_button("提出する")
            if submitted:
                dt_now = datetime.datetime.now()
                dt_now_str = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
                l = [input_name, input_imp, dt_now_str]
                df_tmp = pd.DataFrame(l).T
                df_tmp = df_tmp.rename(columns={0:'氏名', 1:'感想', 2:'時刻'})
                df = pd.read_csv('impression.csv', encoding='utf_8_sig')
                df_out3 = pd.concat([df, df_tmp], axis=0)
                df_out3.to_csv('impression.csv', encoding='utf_8_sig', index=False)
                df_out3

                st.sidebar.success("提出ありがとうございました！")


if __name__ == '__main__':
    main()
