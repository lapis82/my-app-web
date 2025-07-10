import streamlit as st
import folium
from streamlit_folium import st_folium

# 앱 제목
st.title("로마 관광 명소 추천 🏛️")
st.markdown("로마에서 꼭 방문해야 할 유적지 3곳을 지도와 함께 소개합니다!")

# 유적지 정보
landmarks = [
    {
        "name": "콜로세움 (Colosseum)",
        "location": [41.8902, 12.4922],
        "description": "고대 로마의 검투사 경기장으로, 로마 제국의 위엄을 상징합니다."
    },
    {
        "name": "판테온 (Pantheon)",
        "location": [41.8986, 12.4769],
        "description": "모든 신을 위한 신전으로, 현존하는 가장 잘 보존된 고대 로마 건축물입니다."
    },
    {
        "name": "트레비 분수 (Trevi Fountain)",
        "location": [41.9009, 12.4833],
        "description": "동전에 소원을 담는 로마 최고의 분수 명소입니다."
    }
]

# folium 지도 생성
m = folium.Map(location=[41.8933, 12.4829], zoom_start=14)

# 마커 추가
for site in landmarks:
    folium.Marker(
        location=site["location"],
        popup=f"<b>{site['name']}</b><br>{site['description']}",
        tooltip=site["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)


streamlit
folium
streamlit-folium

# 스트림릿에 folium 지도 표시
st_data = st_folium(m, width=700, height=500)
