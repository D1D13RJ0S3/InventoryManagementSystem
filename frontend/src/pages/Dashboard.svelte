<!--
Component: Dashboard.svelte
Description: This component displays a product inventory dashboard with a bar chart showing product prices.
Properties:
  - None
Internal Variables:
  - chart (Chart): Instance of the Chart.js chart.
  - products (array): Array of product data.
  - canvas (HTMLElement): Reference to the canvas element for rendering the chart.
  - interval (number): Interval ID for refreshing data.
Main Functions:
  - fetchData(): Fetches product data from the API, processes it, and updates or renders the chart.
  - renderChart(): Renders the Chart.js bar chart with the fetched product data.
  - updateChart(): Updates the existing chart with new product data.
External Dependencies:
  - Chart.js: Library for rendering charts.
  - tick (svelte): Svelte's tick function to wait for the DOM to update.
-->
<script>
  import { onMount, onDestroy } from 'svelte';
  import { Chart, registerables } from 'chart.js';
  import { tick } from 'svelte';

  // Register all necessary Chart.js components
  Chart.register(...registerables);

  let chart;          // Instance of the chart
  let products = [];  // Product data
  let canvas;         // Reference to the canvas element
  let interval;       // Refresh interval

  const PRODUCTS_LIMIT = 10;

  /**
   * Fetches products from the API, processes the data, and updates or renders the chart.
   */
  async function fetchData() {
    try {
      console.log('Starting API request...');
      const response = await fetch('http://localhost:5000/products');
      if (!response.ok) {
        throw new Error(`Error fetching data: ${response.status} ${response.statusText}`);
      }
      let data = await response.json();
      console.log('Products received:', data);
      products = data
        .sort((a, b) => b.price - a.price)
        .slice(0, PRODUCTS_LIMIT);
      
        if (products.length === 0) {
      products = [
        { name: "P. Muestra 1", price: 100, quantity: 10 },
        { name: "P. Muestra 2", price: 200, quantity: 20 },
        { name: "P. Muestra 3", price: 300, quantity: 30 },
        { name: "P. Muestra 4", price: 400, quantity: 40 },
        { name: "P. Muestra 5", price: 500, quantity: 50 },
      ];
      console.log('Assigned sample products:', products);
    }

    console.log('Filtered products for the chart:', products);

    if (chart) {
      updateChart();
    } else {
      await tick(); 
      renderChart();
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

  /**
   * Renders the Chart.js bar chart for the first time.
   */
   function renderChart() {
  if (canvas && products.length > 0) {
    const ctx = canvas.getContext('2d');
    if (ctx) {
      console.log('Obtained 2D context. Rendering chart...');
      chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: products.map(product => product.name),
          datasets: [
            {
              label: 'Precio',
              data: products.map(product => product.price),
              backgroundColor: 'rgba(54, 162, 235, 0.6)',
              borderColor: 'rgba(54, 162, 235, 1)',
              borderWidth: 1,
              hoverBackgroundColor: 'rgba(54, 162, 235, 0.8)',
              hoverBorderColor: 'rgba(54, 162, 235, 1)',
              hoverBorderWidth: 2,
            },
            {
              label: 'Cantidad',
              data: products.map(product => product.quantity),
              backgroundColor: 'rgba(255, 99, 132, 0.6)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
              hoverBackgroundColor: 'rgba(255, 99, 132, 0.8)',
              hoverBorderColor: 'rgba(255, 99, 132, 1)',
              hoverBorderWidth: 2,
            }
          ]
        },
        options: {
          responsive: true,
          interaction: {
            mode: 'nearest',
            intersect: false,
          },
          plugins: {
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Productos'
            },
            tooltip: {
              callbacks: {
                label: function(context) {
                  const product = products[context.dataIndex];
                  if (context.dataset.label === 'Price') {
                    return [
                      `Name: ${product.name}`,
                      `Price: ${product.price}`,
                      `Quantity: ${product.quantity}`
                    ];
                  } else if (context.dataset.label === 'Quantity') {
                    return [
                      `Name: ${product.name}`,
                      `Quantity: ${product.quantity}`,
                      `Price: ${product.price}`
                    ];
                  }
                }
              },
              backgroundColor: 'rgba(0, 0, 0, 0.7)',
              titleColor: '#fff',
              bodyColor: '#fff',
              borderColor: '#fff',
              borderWidth: 1,
              padding: 10,
            }
          },
          scales: {
            x: {
              ticks: {
                maxRotation: 90,
                minRotation: 45,
                autoSkip: false,
              }
            },
            y: {
              type: 'linear', // Linear scale for Price and Quantity
              display: true,
              position: 'left',
              beginAtZero: true,
              title: {
                display: true,
                text: 'Valor'
              },
              ticks: {
                callback: function(value) {
                  return value;
                }
              }
            }
          },
          animation: {
            duration: 1000,
            easing: 'easeOutBounce',
          },
          onClick: (evt, elements) => {
            if (elements.length > 0) {
              const element = elements[0];
              const datasetIndex = element.datasetIndex;
              const dataIndex = element.index;
              const product = products[dataIndex];
              alert(`Product Name: ${product.name}\nPrice: ${product.price}\nQuantity: ${product.quantity}`);
            }
          }
        }
      });
      console.log('Chart rendered.');
    } else {
      console.error('Could not obtain 2D context from canvas.');
    }
  } else {
    console.error('Canvas element not found or no products to display.');
    console.log('products:', products);
  }
}
  

  /**
   * Updates the existing chart with new product data.
   */
   function updateChart() {
  if (chart) {
    console.log('Updating chart with new data...');
    chart.data.labels = products.map(product => product.name);
    chart.data.datasets[0].data = products.map(product => product.price);
    chart.data.datasets[1].data = products.map(product => product.quantity);
    chart.update();
    console.log('Chart updated.');
  }
}

  onMount(() => {
    fetchData(); // Fetch data on mount

    // Set up interval to refresh every 5 seconds (5000 ms)
    interval = setInterval(fetchData, 5000);
  });

  onDestroy(() => {
    if (chart) {
      chart.destroy();
      console.log('Chart destroyed.');
    }
    if (interval) {
      clearInterval(interval);
      console.log('Refresh interval cleared.');
    }
  });
</script>

<style>
  .dashboard-container {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    width: 100%;
    height: 100%;
  }

  h2 {
    color: #333;
    margin-bottom: 20px;
  }

  canvas {
    max-width: 800px;
    width: 100%;
    height: auto;
    margin-top: 30px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); /* More intense shadow */
    border-radius: 8px;
    background-color: #fff;
  }

  /* Decorative background behind the chart */
  .background-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(54, 162, 235, 0.05); /* Soft semi-transparent color */
    z-index: 0;
    border-radius: 8px;
  }
</style>

<div class="dashboard-container">
  <h2>Inventario de Productos</h2>

  {#if products.length > 0}
    <!-- Decorative background -->
    <div class="background-overlay"></div>
    <!-- Bar Chart -->
    <canvas bind:this={canvas} id="myChart"></canvas>
  {:else}
    <p>Cargando productos...</p>
  {/if}
</div>
