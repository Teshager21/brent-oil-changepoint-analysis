import { useState } from 'react'
import './App.css'
import ChangePointList from "./components/ChangePointList";
import PriceChart from "./components/PriceChart";

function App() {
  return (
    <div>
      <h1>Brent Oil Change Point Dashboard</h1>
      <ChangePointList />
      <PriceChart/>
    </div>
  );
}

export default App
