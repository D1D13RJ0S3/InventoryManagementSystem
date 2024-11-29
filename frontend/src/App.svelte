<script>
	import WelcomePage from './pages/WelcomePage.svelte';
	import Dashboard from './pages/Dashboard.svelte';
  
	let currentPage = 'welcome'; 
  </script>
  
  <main>
	{#if currentPage === 'welcome'}
	  <WelcomePage on:enter={() => currentPage = 'dashboard'} />
	{:else if currentPage === 'dashboard'}
	  <Dashboard />
	{/if}
  </main>
  
  <style>
	main {
	  font-family: 'Roboto', sans-serif;
	  padding: 20px;
	}
  </style>
  