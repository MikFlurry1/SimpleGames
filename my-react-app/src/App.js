import { useEffect } from "react";
import "./App.css";

function App() {
  useEffect(() => {
    const catImage = document.getElementById("cat-image");
    const addscore = document.getElementById("addScore");
    const foodscore = document.getElementById("food-score");

    let i = 0;
    const jRef = { current: 5 };

    const catClicked = () => {
      i++;
      addscore.textContent = "+1";
      document.getElementById("score").textContent = "Play score: " + i;
      setTimeout(() => { addscore.textContent = ""; }, 1000);

      const audioEl = new Audio(
        "https://audio.jukehost.co.uk/zLMskscE4n0hFW4cecg3C4BtO8UU7WfZ"
      );
      audioEl.play();
    };
    catImage.addEventListener("click", catClicked);

    const sushiImage = document.getElementById("sushi");
    const sushiclicked = () => {
      jRef.current++;
      addscore.textContent = "+1";
      foodscore.textContent = "Food score: " + jRef.current;
      setTimeout(() => { addscore.textContent = ""; }, 1000);
    };
    sushiImage.addEventListener("click", sushiclicked);

    const foodInterval = setInterval(() => {
      jRef.current--;
      foodscore.textContent = "Food score: " + jRef.current;
      const gameMessage = document.getElementById("game-message");

      if (jRef.current <= 0) {
        clearInterval(foodInterval);
        document.getElementsByClassName("App-header")[0].className += " bgswitchifyouloose";
        gameMessage.textContent = "YOU LOST";
        gameMessage.style.display = "block";
        gameMessage.className += 'gameMessage';
      } else if (jRef.current >= 50 && i >= 50) {
        clearInterval(foodInterval);
        document.getElementsByClassName("App-header")[0].className += " bgswitch";
        gameMessage.textContent = "YOU WON";
        gameMessage.style.display = "block";
        gameMessage.className += 'gameMessage-';
      }
    }, 1000);
    return () => {
      catImage.removeEventListener("click", catClicked);
      sushiImage.removeEventListener("click", sushiclicked);
      clearInterval(foodInterval);
    };
  }, []);

  return (
    <div className="App">
      <div className="App-header">
        <h1 id="test">Feed or Play with the Cat</h1>
        <h1 id="game-message" style={{ display: "none" }}>YOU LOST</h1> 
        <p>Click the cat to play with the cat (if both are above 50 you win)!!!!!!</p>
        <img
          src="https://cdn.kastatic.org/third_party/javascript-khansrc/live-editor/build/images/animals/cat.png"
          className="App-logo"
          id="cat-image"
          alt="cat"
        />
        <p id="score">Play score: 0</p>
        <p id="food-score">Food score: 5</p>
        <p id="addScore"></p>
        <img
          src="https://cdn.kastatic.org/third_party/javascript-khansrc/live-editor/build/images/food/sushi.png"
          alt="SUSHI IMAGE!!!"
          id="sushi"
        />
        <p id="sushi-text">Click on <span id="sushionly">sushi</span> to feed cat</p>
      </div>
    </div>
  );
}

export default App;
