import React, { useEffect, useState } from "react";
import { fetchChangePoints } from "../api/changePoints";

const ChangePointList = () => {
  const [changePoints, setChangePoints] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchChangePoints()
      .then((data) => setChangePoints(data))
      .catch((err) => setError(err.message));
  }, []);

  if (error) {
    return <p>Error: {error}</p>;
  }

  if (changePoints.length === 0) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h2>Brent Oil Change Points</h2>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Index</th>
            <th>Event</th>
          </tr>
        </thead>
        <tbody>
          {changePoints.map((cp, index) => (
            <tr key={index}>
              <td>{cp.change_point_date}</td>
              <td>{cp.change_point_index}</td>
              <td>{cp.event || "No Event Mapped"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ChangePointList;
