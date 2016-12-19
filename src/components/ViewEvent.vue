<template>
  <div class="view-event-container">
    <div class="view-event" v-if="name">
      <h4>{{ name }}</h4>
      <p>{{ description }}</p>
      <div class="datetime"><strong>When:</strong> {{ startHumanized }}</div>
      <div class="location" v-if="location != ''"><strong>Location:</strong> {{ location }}</div>
      <div class="download">
        <a class="btn btn-default" v-on:click.prevent="download()">Download .ics</a>
        <a class="btn btn-default" v-bind:href="googleLink" 
target="_blank" rel="nofollow">Add to Google Calendar</a>
      </div>
    </div>
    <div class="goback"><router-link :to="{name: 'index'}">Create new event</router-link></div>
  </div>
</template>

<script>
import download from 'in-browser-download';
import icalendar from 'icalendar';
import moment from 'moment';
import parse from 'parse-messy-time';
import uuid from 'uuid';

function toGoogleTime(x) {
  return x.toISOString().replace(/-|:|\.\d\d\d/g, '');
}

export default {
  name: 'viewEvent',
  computed: {
    googleLink() {
      return `
        http://www.google.com/calendar/event?action=TEMPLATE
        &text=${encodeURIComponent(this.name)}
        &dates=
        ${encodeURIComponent(toGoogleTime(this.start.toDate()))}/
        ${encodeURIComponent(toGoogleTime(this.end.toDate()))}
        &details=${encodeURIComponent(this.description)}
        &location=${encodeURIComponent(this.location)}
        &trp=false
        &sprop=
        &sprop=name:
      `.split("\n").map(x => x.trim()).join("");
    },
    startHumanized() {
      return moment(this.start).format('YYYY-MM-DD, HH:mm:ss');
    },
  },
  data() {
    return {
      name: '',
      start: moment(),
      end: moment(),
      description: '',
      location: '',
    };
  },
  created() {
    this.$http.get(`${process.env.API_URL}events/${this.$route.params.slug}`).then(response => {
      this.name = response.body.name;
      this.start = moment(response.body.start);
      this.end = moment(response.body.end);
      this.description = response.body.description;
      this.location = response.body.location;
    }).catch(response => {
      this.$router.push({name: '404'});
    });
  },
  methods: {
    download() {
      const event = new icalendar.VEvent(uuid.v4());
      event.setSummary(this.name);
      event.setDate(this.start.toDate(), this.end.toDate());
      const code = event.toString();
      download(code, 'event.ics');
    },
  }
};
</script>

<style lang="scss" scoped>
.goback {
  text-align: center;
  color: rgb(41, 128, 185);
}
.view-event-container {
  margin: 0px 20px;
  min-width: 350px;
}
.view-event {
  max-width: 700px;
  margin: 0px auto;
  border: 1px rgb(22, 160, 133) solid;
  padding: 10px 20px;
  margin-top: 80px;
  margin-bottom: 15px;

  h4 {
    color: rgb(22, 160, 133);
    font-size: 30px;
  }
  p {
    font-size: 18px;
  }
  .download {
    padding-top: 20px;
  }
}
</style>
