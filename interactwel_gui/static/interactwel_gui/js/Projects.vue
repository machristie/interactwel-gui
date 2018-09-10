<template>
    <ul>
        <li v-for="project in projects" :key="project.projectID">Project: {{ project.name }}</li>
    </ul>
</template>

<script>
import {models, services} from 'django-airavata-api';

export default {
    name: 'projects',
    props: {

    },
    data() {
        return {
            projects: []
        }
    },
    computed: {
        projectCount() {
            return this.projects.length;
        }
    },
    created() {
        services.ProjectService.list()
            .then(projects => this.projects = projects.results);
    }
}
</script>

<style scoped>

</style>

