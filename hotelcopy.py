import requests
import streamlit as st

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "b8b96b10-974d-11ef-8313-8118934c035de7a35b8c-4300-463e-b7de-14140ecf7190"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# while True:
qu = st.text_input("호텔에 대해서 궁금한 것을 저에게 물어보세요>>",'')

if qu !='':

    # if (qu == "나가기") :
    #  break

    demo = classify(qu)

    label = demo["class_name"]
    confidence = demo["confidence"]

    if confidence < 60 :
        st.write("제가 질문을 잘 이해하지 못했어요. 다시 질문해주세요.")

    elif (label == "Reservation") : 
        st.write("호텔 예약과 관련된 정보는 저희 호텔 홈페이지에서 확인하실 수 있습니다.")
        st.write("답변 정확도 :", confidence)

    elif (label == "facility") :
        st.write("저희 호텔에는 헬스장, 수영장, 식당 등이 있습니다. 자세한 사항은 저희 호텔 홈페이지를 참고해주세요.")
        st.write("답변 정확도 :", confidence)

    elif (label == "location") :
        st.write("저희 호텔은 서울특별시 강남구에 위치해있습니다. 강남역 바로 앞에 위치해 있어 교통이 편리합니다.")
        st.write("답변 정확도 :", confidence)

    elif (label == "service") :
        st.write("저희 호텔은 전 객실 와이파이가 가능하며, 룸서비스 및 어메니티 서비스를 이용하실 수 있습니다.")
        st.write("답변 정확도 :", confidence)

    elif (label == "price") :
        st.write("호텔 객실 요금 정보는 저희 호텔 홈페이지에서 확인해주세요.")
        st.write("답변 정확도 :", confidence)

    elif (label == "checkinout") :
        st.write("체크인 시간은 오후 3시이며, 체크아웃 시간은 오후 12시입니다.")
        st.write("답변 정확도 :", confidence)
else:
    st.write ("데이터를 입력해주세요")