<script setup>
import axios from "axios";

import {
  LMap,
  LTileLayer,
  LMarker,
  LIcon,
  LPolyline,
} from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";
</script>
<template>
  <div class="w-full flex flex-col items-center justify-center">
    <h2 class="text-4xl m-4">Swedish Golf Balls</h2>

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

    <div class="w-full md:w-[800px] mt-2">
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
    setClosest5() {
      this.closest5 = this.ikea
        .sort((a, b) => a.nearest_distance > b.nearest_distance)
        .slice(0, 5);
    },
    setFarthest5() {
      this.farthest5 = this.ikea
        .sort((a, b) => a.nearest_distance < b.nearest_distance)
        .slice(0, 5);
    },
  },
  beforeMount() {
    axios.get("ikea_locations.json").then((response) => {
      this.ikea = response.data;
      this.setClosest5();
      this.setFarthest5();
    });

    axios.get("topgolf_locations.json").then((response) => {
      this.topgolf = response.data;
      this.setClosest5();
      this.setFarthest5();
    });
  },
};
</script>
