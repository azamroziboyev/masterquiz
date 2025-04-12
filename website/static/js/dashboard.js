// MasterQuiz Bot Dashboard JavaScript

// Chart colors
const chartColors = [
    '#4dc9f6', '#f67019', '#f53794', '#537bc4',
    '#acc236', '#166a8f', '#00a950', '#58595b', 
    '#8549ba', '#a27ea8', '#a3acb1'
];

// Initialize charts
let testCreatorsChart = null;
let referrersChart = null;

// DOM elements
const lastUpdatedElement = document.getElementById('last-updated');
const totalUsersElement = document.getElementById('total-users');
const activeUsersElement = document.getElementById('active-users');
const totalTestsElement = document.getElementById('total-tests');
const totalReferralsElement = document.getElementById('total-referrals');
const usersTableBody = document.getElementById('users-table-body');
const testsTableBody = document.getElementById('tests-table-body');
const referralsTableBody = document.getElementById('referrals-table-body');

// Function to format numbers
function formatNumber(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// Function to fetch dashboard statistics
async function fetchStatistics() {
    try {
        const response = await fetch('/api/stats');
        const data = await response.json();
        
        // Update dashboard cards
        totalUsersElement.textContent = formatNumber(data.total_users);
        activeUsersElement.textContent = formatNumber(data.active_users);
        totalTestsElement.textContent = formatNumber(data.total_tests);
        totalReferralsElement.textContent = formatNumber(data.total_referrals);
        lastUpdatedElement.textContent = data.updated_at;
        
        return data;
    } catch (error) {
        console.error('Error fetching statistics:', error);
        return null;
    }
}

// Function to fetch users data
async function fetchUsers() {
    try {
        const response = await fetch('/api/users');
        const users = await response.json();
        
        // Clear table
        usersTableBody.innerHTML = '';
        
        if (users.length === 0) {
            usersTableBody.innerHTML = '<tr><td colspan="4" class="text-center">No users found</td></tr>';
            return [];
        }
        
        // Populate table
        users.forEach(user => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${user.id}</td>
                <td>${user.username}</td>
                <td>${user.first_name} ${user.last_name}</td>
                <td>${user.has_invited ? 'Yes' : 'No'}</td>
            `;
            usersTableBody.appendChild(row);
        });
        
        return users;
    } catch (error) {
        console.error('Error fetching users:', error);
        usersTableBody.innerHTML = '<tr><td colspan="4" class="text-center">Error loading users data</td></tr>';
        return [];
    }
}

// Function to fetch tests data
async function fetchTests() {
    try {
        const response = await fetch('/api/tests');
        const testsData = await response.json();
        
        // Clear table
        testsTableBody.innerHTML = '';
        
        if (testsData.length === 0) {
            testsTableBody.innerHTML = '<tr><td colspan="6" class="text-center">No tests found</td></tr>';
            return [];
        }
        
        // Populate table
        testsData.forEach(user => {
            const row = document.createElement('tr');
            
            // Create details content for tests
            let testsDetails = '';
            if (user.tests.length > 0) {
                testsDetails = '<div class="test-details"><h6>Tests:</h6><ol>';
                user.tests.forEach(test => {
                    testsDetails += `<li>${test.name} (${test.questions_count} questions)</li>`;
                });
                testsDetails += '</ol></div>';
            } else {
                testsDetails = '<div class="test-details">No tests available</div>';
            }
            
            row.innerHTML = `
                <td>${user.user_id}</td>
                <td>${user.username}</td>
                <td>${user.full_name}</td>
                <td>${user.test_count}</td>
                <td>${user.total_questions}</td>
                <td>
                    <button class="btn btn-sm btn-outline-info toggle-details">
                        Show Details
                    </button>
                    <div class="details-container d-none">
                        ${testsDetails}
                    </div>
                </td>
            `;
            testsTableBody.appendChild(row);
            
            // Add event listener for details toggle
            const toggleButton = row.querySelector('.toggle-details');
            const detailsContainer = row.querySelector('.details-container');
            
            toggleButton.addEventListener('click', () => {
                detailsContainer.classList.toggle('d-none');
                toggleButton.textContent = detailsContainer.classList.contains('d-none') 
                    ? 'Show Details' 
                    : 'Hide Details';
            });
        });
        
        return testsData;
    } catch (error) {
        console.error('Error fetching tests:', error);
        testsTableBody.innerHTML = '<tr><td colspan="6" class="text-center">Error loading tests data</td></tr>';
        return [];
    }
}

// Function to fetch referrals data
async function fetchReferrals() {
    try {
        const response = await fetch('/api/referrals');
        const referrals = await response.json();
        
        // Clear table
        referralsTableBody.innerHTML = '';
        
        if (referrals.length === 0) {
            referralsTableBody.innerHTML = '<tr><td colspan="3" class="text-center">No referrals found</td></tr>';
            return [];
        }
        
        // Populate table
        referrals.forEach(referral => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${referral.id}</td>
                <td>${referral.referrer_username} (${referral.referrer_name})</td>
                <td>${referral.referred_username} (${referral.referred_name})</td>
            `;
            referralsTableBody.appendChild(row);
        });
        
        return referrals;
    } catch (error) {
        console.error('Error fetching referrals:', error);
        referralsTableBody.innerHTML = '<tr><td colspan="3" class="text-center">Error loading referrals data</td></tr>';
        return [];
    }
}

// Function to update Top Test Creators chart
function updateTestCreatorsChart(testsData) {
    // Process data for top test creators chart
    const testCreators = testsData
        .sort((a, b) => b.test_count - a.test_count)
        .slice(0, 5);
    
    const labels = testCreators.map(creator => creator.username || `User ${creator.user_id}`);
    const data = testCreators.map(creator => creator.test_count);
    
    // Create or update chart
    if (testCreatorsChart) {
        testCreatorsChart.data.labels = labels;
        testCreatorsChart.data.datasets[0].data = data;
        testCreatorsChart.update();
    } else {
        const ctx = document.getElementById('test-creators-chart').getContext('2d');
        testCreatorsChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Tests Created',
                    data: data,
                    backgroundColor: chartColors.slice(0, 5),
                    borderColor: 'rgba(0, 0, 0, 0)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        enabled: true
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            precision: 0
                        }
                    }
                }
            }
        });
    }
}

// Function to update Top Referrers chart
function updateReferrersChart(referralsData) {
    // Process data for top referrers chart
    const referrerCounts = {};
    
    referralsData.forEach(referral => {
        const referrerId = referral.referrer_id;
        const referrerName = referral.referrer_username || `User ${referrerId}`;
        
        if (referrerCounts[referrerId]) {
            referrerCounts[referrerId].count++;
        } else {
            referrerCounts[referrerId] = {
                name: referrerName,
                count: 1
            };
        }
    });
    
    // Convert to array and sort
    const topReferrers = Object.entries(referrerCounts)
        .map(([id, data]) => ({
            id: parseInt(id),
            name: data.name,
            count: data.count
        }))
        .sort((a, b) => b.count - a.count)
        .slice(0, 5);
    
    const labels = topReferrers.map(referrer => referrer.name);
    const data = topReferrers.map(referrer => referrer.count);
    
    // Create or update chart
    if (referrersChart) {
        referrersChart.data.labels = labels;
        referrersChart.data.datasets[0].data = data;
        referrersChart.update();
    } else {
        const ctx = document.getElementById('referrers-chart').getContext('2d');
        referrersChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: labels,
                datasets: [{
                    data: data,
                    backgroundColor: chartColors.slice(0, 5),
                    borderColor: '#1e1e1e',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'right'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const label = context.label || '';
                                const value = context.raw || 0;
                                return `${label}: ${value} referrals`;
                            }
                        }
                    }
                }
            }
        });
    }
}

// Function to load all dashboard data
async function loadDashboardData() {
    // Show loading state
    document.body.style.cursor = 'wait';
    
    // Fetch all data in parallel
    const [stats, users, tests, referrals] = await Promise.all([
        fetchStatistics(),
        fetchUsers(),
        fetchTests(),
        fetchReferrals()
    ]);
    
    // Update charts if we have data
    if (tests && tests.length > 0) {
        updateTestCreatorsChart(tests);
    }
    
    if (referrals && referrals.length > 0) {
        updateReferrersChart(referrals);
    }
    
    // Reset cursor
    document.body.style.cursor = 'default';
}

// Initialize dashboard when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initial load
    loadDashboardData();
    
    // Setup periodic refresh (every 30 seconds)
    setInterval(loadDashboardData, 30000);
});

// Handle navigation
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Remove active class from all links
        document.querySelectorAll('.nav-link').forEach(l => {
            l.classList.remove('active');
        });
        
        // Add active class to clicked link
        this.classList.add('active');
        
        // Show corresponding section
        const targetId = this.getAttribute('href').substring(1);
        
        document.querySelectorAll('section').forEach(section => {
            section.style.display = 'none';
        });
        
        document.getElementById(targetId).style.display = 'block';
    });
});

// Show default section on load
document.querySelectorAll('section').forEach((section, index) => {
    section.style.display = index === 0 ? 'block' : 'none';
});