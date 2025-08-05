import React, { useEffect, useState } from 'react';
import { fetchPrices, fetchChangePoints } from '../api';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine, ResponsiveContainer
} from 'recharts';

export default function PriceChart() {
  const [prices, setPrices] = useState([]);
  const [changePoints, setChangePoints] = useState([]);

  useEffect(() => {
    fetchPrices().then(res => setPrices(res.data));
    fetchChangePoints().then(res => setChangePoints(res.data));
  }, []);

  return (
    <div>
      <h2>Brent Oil Price Timeline</h2>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={prices}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="price" stroke="#8884d8" />

          {changePoints.map((cp, index) => (
            <ReferenceLine
              key={index}
              x={cp.change_point_date}
              stroke="red"
              label={{ value: 'Change', position: 'top', fill: 'red', fontSize: 10 }}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
