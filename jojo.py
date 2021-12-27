import streamlit as st
import random
import time
import streamlit.components.v1 as stc


def main():

    st.header("2022ちょっと奇妙な言葉占い")
    st.markdown("---")
    #結果(result)をリスト化
    result = [
    {'word':'酒！飲まずにはいられないッ！','attention':'飲み過ぎには注意しましょう'},
    {'word':'お前は今まで食ったパンの枚数をおぼえているのか？','attention':'食べ物への感謝の気持ちを大切にしましょう'},
    {'word':'ねーちゃん！あしたっていまさッ！','attention':'中々始められなかったことありませんか？いまがチャンスです'},
    {'word':'「魂」を！賭けよう！グッド','attention':'命は大切にしましょう'},
    {'word':'おれは人間をやめるぞ！ジョジョーーーッ！！','attention':'危険な賭けをしていませんか？思い止まりましょう。'},
    {'word':'勝ったッ！第3部完！','attention':'終わったと思っていること、まだ終わっていないかもしれません。もう一度確認しましょう。'},
    {'word':'ホハハハフフフフヘハハハハフホホアハハハ¥nフハハックックックッヒヒヒヒヒケケケケケ¥nノォホホノォホ','attention':'困りごとに気付けるかもしれません。'},
    {'word':'ぬァァァめるよォオオオオにィィィィ','attention':'熱中しすぎて、周りがよく見えていないかもしれません。一度、冷静になりましょう。'},
    {'word':'あ・・・ありのまま　今起こった事を話すぜ！『おれは　奴の前で階段を登っていたと思ったら　いつのまにか降りていた』','attention':'今あなたは大変混乱していますが状況を正しく認識しています。ありとあらゆる可能性を確認しましょう。'},
    {'word':'『山を登る時　ルートもわからん！頂上がどこにあるかもわからんでは遭難は確実なんじゃ！』確実！そうコーラを飲んだらゲップが出るっていうくらい確実じゃッ！','attention':'あなたは目標を見失っています。立ち止まって、目標を再確認しましょう。'},
    {'word':'君がッ　泣くまで　殴るのをやめないッ！','attention':'感情が爆発しそうかもしれませんが、やり過ぎには気をつけましょう。'}]

    display = [
        {'disp':'スピードワゴンはクールに占うぜ',
         'disp':'魂を占うかい？',
         'disp':'オラオラオラオラッ',
         'disp':'無駄無駄無駄無駄ッ！',
         'disp':'チュミミ〜〜〜ン'}]

    name = random.choice(display)

    button = st.button(name)['disp']

    if button:
        my_bar = st.progress(0)
        st.balloons()
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)

        #resultからランダムに選ぶ
        omikuji = random.choice(result)

        st.markdown("# "+omikuji['word'])
        # stc.html("<p style='font-size: 50pt;, color: #ff0000;, font-family:MS Pゴシック,sans-serif;'>" + omikuji['word'])
        st.markdown(omikuji['attention'])


if __name__ == '__main__':
    main()