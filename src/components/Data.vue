<script setup>
import axios from "axios";
import Accordion from "primevue/accordion";
import AccordionTab from "primevue/accordiontab";
import Slider from 'primevue/slider';

import {
  LMap,
  LTileLayer,
  LMarker,
  LIcon,
  LPolyline,
  LControl,
} from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";
</script>
<template>
  <div class="w-full flex flex-col items-center justify-center">
    <h2 class="text-4xl m-4">Swedish Golf Balls</h2>
    <div class="text-xl m-4">Is there always a Topgolf right next to IKEA, or is it just me?</div>

    <!-- Map Div -->
    <div
      class="md:w-[700px] lg:w-[800px] md:h-[600px] w-full h-[500px] px-2 md:p-0"
    >
      <l-map ref="map" v-model:zoom="zoom" :center="center">
        <l-tile-layer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          layer-type="base"
          name="OpenStreetMap"
        ></l-tile-layer>
        <l-control
          class="bg-white text-black text-sm p-2 opacity-80"
          position="bottomleft"
        >
          <div class="flex justify-between mb-1">
            <img
              class="h-6 mr-1"
              src="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-yellow.png"
            />
            IKEA
          </div>
          <div class="flex justify-between">
            <img
              class="h-6 mr-1"
              src="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-black.png"
            />Topgolf
          </div>
        </l-control>
        <l-marker
          :lat-lng="[store.lat, store.lon]"
          v-for="store of ikea"
          @click="
            setLine(store.lat, store.lon, store.nearest_lat, store.nearest_lon)
          "
          ><l-icon
            :icon-url="'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-yellow.png'"
            :shadow-url="'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png'"
            :icon-size="[25, 41]"
            :icon-anchor="[12, 41]"
            :shadow-size="[41, 41]"
          ></l-icon
        ></l-marker>
        <l-marker
          :lat-lng="[store.lat, store.lon]"
          v-for="store of topgolf"
          @click="
            setLine(store.lat, store.lon, store.nearest_lat, store.nearest_lon)
          "
        >
          <l-icon
            :icon-url="'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-black.png'"
            :shadow-url="'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png'"
            :icon-size="[25, 41]"
            :icon-anchor="[12, 41]"
            :shadow-size="[41, 41]"
          ></l-icon>
        </l-marker>
        <l-polyline
          :key="lineIteration"
          :lat-lngs="lineCoords.coords"
          color="red"
        ></l-polyline>
      </l-map>
    </div>

    <div class="w-full md:w-[800px] mt-2 mb-16">
      <div class="grid grid-cols-1 md:grid-cols-2 w-full">
        <!-- Closest 5 Div -->
        <div class="w-full md:w-96 px-4">
          <h2 class="text-2xl border-b border-slate-400">
            IKEA stores nearest to Topgolf
          </h2>
          <div
            class="flex justify-between py-1 my-1 text-xl hover:bg-slate-700"
            v-for="store in closest5"
            @click="
              setLine(
                store.lat,
                store.lon,
                store.nearest_lat,
                store.nearest_lon
              )
            "
          >
            <div class="">{{ store.city }}</div>
            <div class="">
              {{ Math.round(store.nearest_distance * 100) / 100 }} miles
            </div>
          </div>
        </div>
        <!-- Farthest 5 Div -->
        <div class="w-full md:w-96 px-4 mt-8 md:mt-0">
          <h2 class="text-2xl border-b border-slate-400">
            IKEA stores farthest from Topgolf
          </h2>
          <div
            class="flex justify-between py-1 my-1 text-xl hover:bg-slate-700"
            v-for="store in farthest5"
            @click="
              setLine(
                store.lat,
                store.lon,
                store.nearest_lat,
                store.nearest_lon
              )
            "
          >
            <div class="">{{ store.city }}</div>
            <div class="">
              {{ Math.round(store.nearest_distance * 100) / 100 }} miles
            </div>
          </div>
        </div>
      </div>
      <div class="w-full border border-dashed border-slate-200 p-4 text-center text-xl md:text-3xl my-8">
        {{ closePercent }}% of IKEA stores are within {{ closeRange }} miles of a Topgolf!
        <slider v-model="closeRange" class="w-full mt-4" @change="setClosePercent(closeRange)"/>
      </div>
      <accordion class="mt-8">
        <accordion-tab
          :pt="{ headerAction: { class: 'hover:text-gray-200' } }"
          header="What?"
          >We're looking at the locations of all IKEA and Topgolf locations in
          the United States, to see if they are generally located near each
          other.
          <br /><br/>
          Since there are so many more Topgolf locations, it makes sense to look
          at it from the perspective of IKEA - how close is the nearest Topgolf?
        </accordion-tab>
        <accordion-tab
          :pt="{ headerAction: { class: 'hover:text-gray-200' } }"
          header="Why?"
          >While driving around the Eastern US this summer, I noticed an IKEA
          and Topgolf near to each other. And then another, and another.
          Frequently enough to make we wonder, "Is there something to this?" <br/><br/> It may just be a coincidence, 
          but I was curious about building something
          with Leaflet so here we are.</accordion-tab
        >
        <accordion-tab
          :pt="{ headerAction: { class: 'hover:text-gray-200' } }"
          header="How?"
          >Swedish Golf Balls was built using Vue and Leaflet. <br/><br/>  Data was compiled using Python (BeautifulSoup, GeoPy).<br/> <br/> If you're curious, <a class="underline hover:text-blue-400" href="https://github.com/johndeboer/swedish-golf-balls">check out the repo on Github.</a></accordion-tab
        >
      </accordion>
      <div class="w-full text-center mt-4">Made by <a class="underline hover:text-blue-400" href="https://github.com/johndeboer">John DeBoer</a></div>
    </div>
  </div>
</template>

<script>
export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LIcon,
    LPolyline,
    LControl,
  },
  data() {
    return {
      zoom: 4,
      center: [40, -96],
      ikea: [],
      topgolf: [],
      lineCoords: { coords: [] },
      lineIteration: 0,
      closest5: [],
      farthest5: [],
      closePercent: 0,
      closeRange: 20,
    };
  },
  methods: {
    setLine(aLat, aLon, bLat, bLon) {
      this.lineCoords.coords.length = 0;
      this.lineCoords.coords.push([aLat, aLon]);
      this.lineCoords.coords.push([bLat, bLon]);
      this.lineIteration += 1;

      this.$refs.map.leafletObject.fitBounds([
        [aLat, aLon],
        [bLat, bLon],
      ]);
    },
    setClosePercent(range){
      const close = this.ikea.filter((a) => a.nearest_distance <= range).length;
      this.closePercent = Math.round((close / this.ikea.length)*100)
    },
    setClosest5() {
      this.closest5 = this.ikea
        .sort((a, b) => a.nearest_distance - b.nearest_distance)
        .slice(0, 5);
    },
    setFarthest5() {
      this.farthest5 = this.ikea
        .sort((a, b) => b.nearest_distance - a.nearest_distance)
        .slice(0, 5);
    },
  },
  beforeMount() {
    axios.get("ikea_locations.json").then((response) => {
      this.ikea = response.data;
      this.setClosest5();
      this.setFarthest5();
      this.setClosePercent(this.closeRange);
    });

    axios.get("topgolf_locations.json").then((response) => {
      this.topgolf = response.data;
      this.setClosest5();
      this.setFarthest5();
      this.setClosePercent(this.closeRange);
    });
  },
};
</script>
