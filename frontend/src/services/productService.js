const QUERY_BASE_URL = 'http://localhost:8002/api/v1/products';
const COMMAND_BASE_URL = 'http://localhost:8001/api/v1/products';

export async function fetchProducts() {
  const response = await fetch(QUERY_BASE_URL);
  return response.json();
}

export async function createProduct(productData) {
  const response = await fetch(COMMAND_BASE_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(productData),
  });
  return response.json();
}

export async function updateProduct(id, updatedData) {
  const response = await fetch(`${COMMAND_BASE_URL}/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(updatedData),
  });
  return response.json();
}

export async function deleteProduct(id) {
  await fetch(`${COMMAND_BASE_URL}/${id}`, {
    method: 'DELETE',
  });
}
