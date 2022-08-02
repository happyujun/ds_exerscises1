import streamlit as st
import sqlite3

con = sqlite3.connect('db.db')
cur = con.cursor()

#unique키 어케 설정하기
def check_uid(uid):
    cur.execute(f"SELECT COUNT(*) FROM users WHERE uid='{uid}'") #text값은 반드시 따옴표로 둘러싸야함
    res = cur.fetchone()
    return res[0]

def check_uemail(uemail):
    cur.execute(f"SELECT COUNT(*) FROM users WHERE uemail='{uemail}'") #text값은 반드시 따옴표로 둘러싸야함
    res = cur.fetchone()
    return res[0]

st.subheader('회원가입 폼')

with st.form('my_form', clear_on_submit=True):
    st.info('다음 양식을 모두 입력 후 제출합니다.')
    uid = st.text_input('아이디', max_chars=12).strip()
    uname = st.text_input('성명', max_chars=10).strip()
    uemail = st.text_input('이메일').strip()
    upw = st.text_input('비밀번호', type='password').strip()
    upw_chk = st.text_input('비밀번호 확인', type='password').strip()
    ubd = st.date_input('생년월일')
    ugender = st.radio('성별', options=['남', '여'], horizontal=True)

    submitted = st.form_submit_button('제출')
    if submitted:
        if upw != upw_chk:  # 이런 거 코딩할 때는 부정적으로 해야한다. 그래야 나중에 편하다. 같다면 진행해야지~이러면 계속 함.
            st.warning('비밀번호를 확인하세요!')
            st.stop()

        if check_uid(uid): #1이면 같은아이디가 존재하므로 진행시키면 안된다.
            st.warning('동일한 아이디가 존재합니다.')
            st.stop()

        if check_uemail(uemail): #1이면 같은 메일이 존재하므로 진행시키면 안된다.
            st.warning('동일한 이메일이 존재합니다.')
            st.stop()

        st.success(f'{uid} {uname} {uemail} {upw} {ubd} {ugender}')
        cur.execute(f"INSERT INTO users VALUES ("
                    f"'{uid}','{uname}', '{uemail}', '{upw}',"
                    f"'{ubd}','{ugender}',CURRENT_DATE)")
        con.commit()

