/**
 * Function to fetch products from the API.
 * 
 * This function sends an HTTP GET request to the specified URL to
 * retrieve a list of products from the server. If successful,
 * it returns the product data in JSON format. If an error occurs,
 * it catches the error, logs it to the console, and returns an empty array.
 * 
 * @returns {Promise<Array>} A promise that resolves to an array of products.
 */
export async function fetchProducts() {
  try {
    // Sends an HTTP GET request to the specified URL
    const response = await fetch('http://localhost:5000/products');
    
    // Checks if the response is not successful
    if (!response.ok) {
      throw new Error('Error al cargar los productos');
    }
    
    // Returns the product data in JSON format
    return await response.json();
  } catch (error) {
    // Catches and logs any error that occurs during the request
    console.error('Error al obtener productos:', error);
    
    // Returns an empty array in case of error
    return [];
  }
}