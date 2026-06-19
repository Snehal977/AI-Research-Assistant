import plotly.express as px
def chunk_distribution_chart(chunks):
    chunk_lengths=[
        len(chunk)for chunk in chunks
    ]
    fig=px.bar(x=list(range(1,len(chunk_lengths)+1)),y=chunk_lengths,labels={"x":"chunk number","y":"chunk length"},title="chunk size distribution")
    return fig