import React, { useEffect, useState } from 'react';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine, ResponsiveContainer
} from 'recharts';
import { fetchPrices, fetchChangePoints } from '../api';

export default function PriceChart() {
  const [prices, setPrices] = useState([]);
  const [changePoints, setChangePoints] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadData() {
      try {
        const priceRes = await fetchPrices();

        const changePointRes = await fetchChangePoints();

        const cleanedPrices = priceRes.data.map(p => ({
          ...p,
          date: p.Date.slice(0, 10), // Ensure YYYY-MM-DD format
          price: Number(p.Price), // Ensure numeric
        }));

        const significantCPs = changePointRes.data.filter(cp =>
          cp.event?.toLowerCase().includes("significant")
        ).map(cp => ({
          ...cp,
          change_point_date: cp.change_point_date.slice(0, 10), // Ensure format
        }));

        setPrices(cleanedPrices);
        setChangePoints(significantCPs);
        setLoading(false);
      } catch (error) {
        console.error("❌ Failed to load data:", error);
        setLoading(false);
      }
    }

    loadData();
  }, []);

  if (loading) return <p>Loading chart...</p>;
  if (prices.length === 0) return <p>No price data available.</p>;

  return (
    <div>
      <h2>Brent Oil Price Timeline</h2>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={prices}>
          <CartesianGrid stroke="#ccc" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="price" stroke="#0070f3" dot={false} />

          {changePoints.map((cp, i) => (
            <ReferenceLine
              key={i}
              x={cp.change_point_date}
              stroke="red"
              strokeDasharray="3 3"
              label={{
                value: `Δ ≈ ${cp.description?.split("≈")[1]?.trim() || ""}`,
                position: 'top',
                fill: 'red',
                fontSize: 10
              }}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
