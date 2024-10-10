document 
 .getElementById("searchForm") 
 .addEventListener("submit", async function (e) { 
 e.preventDefault();
 // Get the query from the input field 
 const query = document.getElementById("query").value;
 // Make sure there's a query entered 
 if (query.trim() === "") { 
 alert("Please enter a search term");
 return;
 } 
 // Solr query URL 
 const solrUrl = `http://localhost:8983/solr/employee_data/select?q=${query}&wt=json`;
 try { 
 // Fetch data from Solr 
 const response = await fetch(solrUrl);
 const data = await response.json();
 // Display results 
 displayResults(data.response.docs);
 } catch (error) { 
 console.error("Error fetching data:", error);
 alert("Failed to fetch data from Solr");
 } 
 });
function displayResults(docs) { 
 const resultsDiv = document.getElementById("results");
 resultsDiv.innerHTML = "";
 if (docs.length === 0) { 
 resultsDiv.innerHTML = "<p>No results found</p>";
 return;
 } 
 docs.forEach((doc) => { 
 const resultItem = document.createElement("div");
 resultItem.classList.add("result-item");
 // Extract fields from the document, ensuring to access the first item in arrays 
 resultItem.innerHTML = ` 
 <p><strong>Employee ID:</strong> ${doc.Employee_ID[0]}</p> 
 <p><strong>Full Name:</strong> ${doc.Full_Name[0]}</p> 
 <p><strong>Job Title:</strong> ${doc.Job_Title[0]}</p> 
 <p><strong>Department:</strong> ${doc.Department[0]}</p> 
 <p><strong>Gender:</strong> ${doc.Gender[0]}</p> 
 <p><strong>Ethnicity:</strong> ${doc.Ethnicity[0]}</p> 
 <p><strong>Age:</strong> ${doc.Age[0]}</p> 
 <p><strong>Country:</strong> ${doc.Country[0]}</p> 
 <p><strong>City:</strong> ${doc.City[0]}</p> 
 <p><strong>Hire Date:</strong> ${doc.Hire_Date[0]}</p> 
 <p><strong>Annual Salary:</strong> ${doc.Annual_Salary[0]}</p> 
 <p><strong>Bonus:</strong> ${doc.Bonus__[0]}</p> 
 `;
 resultsDiv.appendChild(resultItem);
 });
} 
