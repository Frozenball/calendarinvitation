<template>
  <div class="container">
    <img src="static/logo.png" alt="Create calendar event" />
    <p>Use this tool for creating <a href="https://en.wikipedia.org/wiki/ICalendar">iCalendar files</a> that you can share with others.</p>
    <div class="contents">
      <form v-on:submit.prevent="create()">
        <label class="biginput">
          <div class="title">Event name</div>
          <input required class="input" type="text" v-model="eventName" value="" placeholder="BBQ at my place" autofocus="true">
        </label>
        <label class="biginput">
          <div class="title">Event description</div>
          <textarea rows="4" class="input" v-model="eventDescription" placeholder="Let's meet for some dinner. Bring some drinks and snacks."></textarea>
        </label>
        <label class="biginput">
          <div class="title">Event time</div>
          <input required class="input" type="text" v-model="eventTime" value="" placeholder="Friday, 17:00">
          <div class="datetime" v-if="eventTime != ''">{{ humanDatetime }}</div>
          <div class="datetime datetime-preview" v-if="eventTime == ''">Examples: 23:00, next monday, 5th of january</div>
        </label>
        <label class="biginput">
          <div class="title">Event location</div>
          <input class="input" type="text" v-model="eventLocation" value="" placeholder="Kamppi, Helsinki">
        </label>
<!--         <label class="biginput">
          <div class="title">Event duration</div>
          <input class="input" type="text" v-model="eventDuration" value="" placeholder="1 hour">
        </label> -->
        <!-- <pre>{{ code }}</pre> -->
        <button class="btn btn-large btn-default" type="submit">Create</button>
      </form>
    </div>
  </div>
</template>

<script>
import download from 'in-browser-download';
import icalendar from 'icalendar';
import moment from 'moment';
import parse from 'parse-messy-time';
import uuid from 'uuid';

export default {
  name: 'createEvent',
  computed: {
    datetime() {
      return parse(this.eventTime);
    },
    humanDatetime() {
      return moment(this.datetime).format('YYYY-MM-DD, HH:mm:ss');
    },
    code() {
      const event = new icalendar.VEvent(uuid.v4());
      event.setSummary(this.eventName);
      event.setDate(this.datetime, moment(this.datetime).add(1, 'hour').toDate());
      event.setLocation(this.eventLocation);
      event.setDescription(this.eventDescription);
      return event.toString();
    },
  },
  data() {
    return {
      eventName: '',
      eventLocation: '',
      eventTime: '',
      eventDescription: '',
      eventDuration: ''
    };
  },
  methods: {
    create() {
      if (!this.eventName) {
        return;
      }

      fetch(`${process.env.API_URL}events`, {
        method: 'POST', 
        mode: 'cors',
        body: JSON.stringify({
          name: this.eventName,
          start: this.datetime,
          end: moment(this.datetime).add(1, 'hour').toDate(),
          location: this.eventLocation,
          description: this.eventDescription,
        }),
        headers: new Headers({
          'Content-Type': 'application/json',
        })
      })
      .then(x => x.json())
      .then(data => {
        this.$router.push({name: 'view', params: {slug: data.slug}});
      })
      .catch(error => {
        alert('Error occured! :-(');
      });
    },
    download() {
      download(this.code, 'event.ics');
    },
  },
};
</script>

<style lang="scss" scoped>
.container > p {
  padding: 0px 20px;
}
.container img {
  width: 100%;
  margin-top: 100px;
  padding: 20px;
}
.datetime {
  padding: 5px 0px;
  font-size: 16px;
  font-weight: normal;
  &.datetime-preview {
    color: gray;
  }
}

.biginput {
  width: 100%;
  margin-bottom: 15px;
  .title {
    font-size: 18px;
  }
  input {
    width: 100%;
    font-size: 30px;
    font-weight: normal;
  }
  textarea {
    width: 100%;
    font-size: 16px;
    font-weight: normal;
    padding: 6px;
  }
}
.contents {
  padding: 20px;
}
</style>
