import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Streamlitアプリケーションのタイトルを設定
st.title('y = x^2 の3Dプロット')

# x軸の範囲を設定（-10から10まで）
x = np.linspace(-10, 10, 400)

# y = x^2 の計算
y_positive = x**2
y_negative = -x**2

# 3Dプロットを作成
fig = go.Figure()

# y > 0 の領域（y = x^2）
fig.add_trace(go.Surface(x=x, y=y_positive, z=np.zeros_like(x), colorscale='Viridis', opacity=0.8, showscale=False))

# y < 0 の領域（y = -x^2）
fig.add_trace(go.Surface(x=x, y=y_negative, z=np.zeros_like(x), colorscale='Viridis', opacity=0.8, showscale=False))

# レイアウトの設定
fig.update_layout(scene=dict(zaxis=dict(range=[-100, 100])),
                  margin=dict(l=0, r=0, b=0, t=0))

# 3Dプロットを表示
st.plotly_chart(fig)
#上記のコードでは、Streamlitアプリケーションを作成し、指定された条件に基づいてy = x^2 の3Dプロットを作成しています。アプリケーションを実行するには、ターミナルまたはコマンドプロンプトで以下のコマンドを実行します：

bash
Copy code
streamlit run app.py
#これにより、ローカルでStreamlitアプリケーションが起動し、ブラウザでアクセスできるようになります。アプリケーション内で90°傾けたグラフを見ることができます。





