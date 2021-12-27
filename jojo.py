import streamlit as st
import random
import time
import datetime
import pandas as pd
import streamlit.components.v1 as stc


def main():

    if 'count' not in st.session_state: 
        st.session_state.count = 0 #countがsession_stateに追加されていない場合，0で初期化


    st.header("2022ちょっと奇妙な言葉占い")
    st.markdown("---")
    #結果(result)をリスト化
    result = [
    {'word':'酒！飲まずにはいられないッ！','attention':'酒に頼りすぎていませんか？飲む以外に出來ることをやりましょう。', 'class':'凶'},
    {'word':'お前は今まで食ったパンの枚数をおぼえているのか？','attention':'食べ物への感謝の気持ちを大切にしましょう', 'class':'中吉'},
    {'word':'ねーちゃん！あしたっていまさッ！','attention':'中々始められなかったことありませんか？いまがチャンスです', 'class':'大吉'},
    {'word':'「魂」を！賭けよう！グッド','attention':'大切な決断をする時です。よく考えて決めましょう。', 'class':'吉'},
    {'word':'おれは人間をやめるぞ！ジョジョーーーッ！！','attention':'危険な賭けをしていませんか？思い止まりましょう。', 'class':'大凶'},
    {'word':'勝ったッ！第3部完！','attention':'終わったと思っていること、まだ終わっていないかもしれません。もう一度確認しましょう。', 'class':'凶'},
    {'word':'ホハハハフフフフヘハハハハフホホアハハハ  フハハックックックッヒヒヒヒヒケケケケケ  ノォホホノォホ','attention':'ずっと困っていた事が解決できるでしょう。', 'class':'吉'},
    {'word':'ぬァァァめるよォオオオオにィィィィ','attention':'熱中しすぎて、周りがよく見えていないかもしれません。一度、冷静になりましょう。', 'class':'小吉'},
    {'word':'あ・・・ありのまま　今起こった事を話すぜ！『おれは　奴の前で階段を登っていたと思ったら　いつのまにか降りていた』','attention':'今あなたは大変混乱していますが状況を正しく認識しています。ありとあらゆる可能性を確認しましょう。','class':'吉'},
    {'word':'『山を登る時　ルートもわからん！頂上がどこにあるかもわからんでは遭難は確実なんじゃ！』確実！そうコーラを飲んだらゲップが出るっていうくらい確実じゃッ！','attention':'あなたは目標を見失っています。立ち止まって、目標を再確認しましょう。', 'class':'吉'},
    {'word':'君がッ　泣くまで　殴るのをやめないッ！','attention':'感情が爆発しそうかもしれませんが、やり過ぎには気をつけましょう。', 'class':'吉'}]

    display = [
        {'disp':'スピードワゴンはクールに占うぜ',
         'disp':'オラオラオラオラッ',
         'disp':'無駄無駄無駄無駄ッ！'}]

    name = random.choice(display)


    button = st.button('オラオラオラオラッ')

    if button:
        st.session_state.count += 1 #値の更新

        my_bar = st.progress(0)
        st.balloons()
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
        my_bar.progress(0)

        #resultからランダムに選ぶ
        omikuji = random.choice(result)

        st.markdown("# "+omikuji['word'])
        st.markdown("## "+omikuji['class'])

        # stc.html("<p style='font-size: 50pt;, color: #ff0000;, font-family:MS Pゴシック,sans-serif;'>" + omikuji['word'])
        st.markdown(omikuji['attention'])


    if st.session_state.count>10:
        st.markdown(str(st.session_state.count)+"回実行しています"
                    """
                    大分気に入ってもらえたようですね！
                    """)

    if st.session_state.count>0:
        st.markdown("""
                    ---
                    """)
        with st.form("感想記入欄"):
            st.write("もしよかったら感想やご意見をください。")
            input_name = st.text_input("氏名")
            input_imp = st.text_area("感想")

            # Every form must have a submit button.
            submitted = st.form_submit_button("提出する")
            if submitted:
                dt_now = datetime.datetime.now()
                dt_now_str = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
                l = [input_name, input_imp, dt_now_str]
                df_tmp = pd.DataFrame(l).T
                df_tmp = df_tmp.rename(columns={0:'氏名', 1:'感想', 2:'時刻'})
                df = pd.read_csv('impression.csv', encoding='utf_8_sig')
                df_out = pd.concat([df, df_tmp], axis=0)
                df_out.to_csv('impression.csv', encoding='utf_8_sig', index=False)


if __name__ == '__main__':
    main()