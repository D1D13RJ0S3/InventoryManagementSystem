/**
 * Formats a numerical value to Colombian Peso (COP) currency format.
 * 
 * This function takes a numerical value and returns it formatted as a currency string in Colombian Pesos.
 * It utilizes the Intl.NumberFormat API with the 'es-CO' locale and 'COP' currency.
 * 
 * @param {number} value - The numerical value to format.
 * @returns {string} The formatted currency string in COP.
 */
export function formatToCOP(value) {
  return new Intl.NumberFormat('es-CO', {
    style: 'currency',
    currency: 'COP',
  }).format(value);
}