import App from './src/App'

const e = React.createElement;
const domContainer = document.querySelector('classroom_app_container');

ReactDOM.render(e(App), domContainer);


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
