import gradio as gr


myscript = """
async () => {
    // set testFn() function on globalThis, so you html onlclick can access it
    // const d3 = await import("https://cdn.jsdelivr.net/npm/d3@7/+esm");
    // globalThis.d3 = d3;
    // or
    const script = document.createElement("script");
    script.onload = () =>  console.log("d3 loaded") ;
    script.src = "https://cdn.jsdelivr.net/npm/d3@7";
    document.head.appendChild(script);

    getLocation = () => {
        return new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(
            function (position) {
                console.log("Latitude is :", position.coords.latitude);
                console.log("Longitude is :", position.coords.longitude);
                let out = String(position.coords.latitude)+ "," + String(position.coords.longitude);
                resolve(out);
            },
            function (error) {
                reject(error);
            }
            );
        });
    };
    const myout = await getLocation();
    console.log("out = ",myout);
    return myout;
}
"""


with gr.Blocks() as demo:   
    x = gr.Textbox(id="outtext")
    # run script function on load,
    b = gr.Button(label="Start")
    b.click(None, None, x, _js=myscript)

demo.launch()