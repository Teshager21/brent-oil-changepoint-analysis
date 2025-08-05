export async function fetchChangePoints() {
  const response = await fetch("http://localhost:5000/api/change-points");
  if (!response.ok) {
    throw new Error("Failed to fetch change points");
  }
  return response.json();
}
