<template>
    <div class="page-inner">
        <div class="d-flex align-items-left align-items-md-center flex-column flex-md-row pt-2 pb-4">
            <div>
                <h3 class="fw-bold mb-3">Dashboard</h3>
                <span class="op-7 mb-2">Inbound Courier > <a class="text-primary fw-bold" href="#">Details</a></span>
            </div>
            <div class="ms-md-auto py-2 py-md-0">
                <a href="#" class="btn btn-label-info btn-round me-2">Manage</a>
                <a href="#" class="btn btn-primary btn-round">Add Customer</a>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

// Type for window.appConfig
declare global {
    interface Window {
        appConfig: {
            accessToken: string;
            userId: string;
        };
    }
}

interface DashboardStats {
    users: number;
    products: number;
    sales: number;
    items: number;
}

export default defineComponent({
    name: 'HomeComponent',
    data() {
        return {
            accessToken: window.appConfig.accessToken,
            userId: window.appConfig.userId,
            loading: false,
            stats: {
                users: 0,
                products: 0,
                sales: 0,
                items: 0
            } as DashboardStats
        };
    },
    methods: {
        async fetchDashboardStats() {
            this.loading = true;
            try {
                const response = await fetch('/api/dashboard/stats/', {
                    headers: {
                        'Authorization': `Bearer ${this.accessToken}`,
                        'Content-Type': 'application/json'
                    }
                });

                if (response.ok) {
                    this.stats = await response.json();
                }
            } catch (error) {
                console.error('Error fetching dashboard stats:', error);
            } finally {
                this.loading = false;
            }
        }
    },
    mounted() {
        console.log('Component mounted with user ID:', this.userId);
        this.fetchDashboardStats();
    }
});
</script>

<style scoped>

</style>