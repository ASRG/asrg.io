import React, { useState } from "react";
import "./App.scss";
import "./main.css";
import CountUp from "react-countup";
import Logo from "./logo.png";
import { Map, Marker, Popup, TileLayer } from "react-leaflet";
import data from "./data/data.json";
import dayjs from "dayjs";

function App() {
  let total = 0;
  let locations = data.length;
  let meetings = 0;
  data.forEach(d => {
    total += d.members;
    meetings += d.past;
  });

  return (
    <div className="flex w-full flex-col">
      <Nav />
      <div className="flex w-full flex-col justify-between lg:flex-row px-3 py-6">
        <Widget total={total} title="Members" />
        <Widget total={locations} title="Locations" />
        <Widget total={meetings} title="Meetings" />
        <Widget total={2.5} title="Years Old" />
      </div>
      <MapContainer />
      <Footer />
    </div>
  );
}

const Nav = () => {
  return (
    <nav className="bg-darkBlue2 w-full py-4 flex items-center md:justify-between justify-center flex-wrap shadow">
      <div className="flex w-full justify-center items-center flex-shrink-0 text-gray-600 ml-4 m3-6">
        <a href="https://asrg.io/">
          <img src={Logo} className="logo mr-3" alt="ASRG Logo" />
        </a>
      </div>
    </nav>
  );
};

const MapContainer = () => {
  const position = [48.79, 9.19]; // start position in Stuttgart
  let markers = data.map(d => ({
    position: d.location,
    markup: (
      <div>
        <div className="font-bold text-base text-blueGray">{d.name}</div>
        <div className="flex flex-col pt-2 leading-normal text-sm	">
          Created: {dayjs.unix(d.created / 1000).format("MMMM D YYYY")}
          <br />
          Members: {d.members}
          <br />
          Past Events: {d.past}
          <br />
          Upcoming Events: {d.upcoming}
          <br />
          Last Event: {d.lastEvent}
          <br />
          <div className={`${d.active ? "text-green-800" : "text-gray-800"}`}>
            Active
          </div>
          <div className="pt-2 flex w-full justify-center text-white">
            <a
              href={d.link}
              className="uppercase bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              style={{ color: "white!important" }}
            >
              join
            </a>
          </div>
        </div>
      </div>
    )
  }));

  return (
    <div className="w-full px-6 py-3 flex justify-center">
      <div className="bg-darkBlue2 border w-full rounded">
        <div className="font-bold text-xl text-gray-200 mb-2 p-6">
          ASRG Locations
        </div>

        <Map center={position} zoom={5}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          />
          {markers.map((m, i) => (
            <Marker key={"marker-" + i} position={m.position}>
              <Popup>{m.markup}</Popup>
            </Marker>
          ))}
        </Map>
      </div>
    </div>
  );
};

const Widget = ({ total, title }) => {
  return (
    <div className="px-2 w-full py-2 lg:py-0">
      <div className="w-full bg-darkBlue2 px-3 lg:w-full rounded overflow-hidden border">
        <div className=" px-6 py-4">
          <div className="font-bold text-xl text-gray-300 mb-2">
            <CountUp decimal="," end={total} duration={2} />
          </div>
          <p className="text-gray-400 text-base">{title}</p>
        </div>
      </div>
    </div>
  );
};

const Footer = () => {
  return (
    <footer className="flex justify-center w-full bg-darkBlue1 border-t-2 border-darkBlue2 p-6 mt-10">
      <div className="w-full lg:w-6/12 flex flex-col items-center justify-center">
        <div className="flex justify-center flex-col w-6/12 sm:w-5/12 md:w-5/12 lg:w-3/12 ">
          <div className="flex w-full flex-row flex-wrap justify-between">
            <Icon
              link="https://join.slack.com/t/asrg/shared_invite/enQtNjMyMzAyMDM4MjI1LTM2Njc3MWRkNWI1NjkwYmQ4NDRkZjYwYmE2MzcyMWY3Y2IwZjc1YTAzYjQxM2M0NzdhOGEzNjNmYjNkM2EzZWM"
              icon="slack"
            />
            <Icon link="https://twitter.com/AutoSecResGroup" icon="twitter" />
            <Icon
              link="https://facebook.com/ASRG-Automotive-Security-Research-Group-1454803571254832/"
              icon="facebook"
            />
            <Icon
              link="https://www.linkedin.com/company/automotive-security-research-group/"
              icon="linkedin"
            />
            <Icon link="mailto:hello@asrg.io" icon="envelope" />
          </div>
        </div>
        <div className="flex w-full sm:w-full  md:w-full lg:w-10/12 xl:w-8/12 justify-center">
          <div className="flex w-full m-6">
            <div className="flex w-full flex-col md:flex-row items-center justify-center">
              <a href="https://asrg.io/">
                <div className="px-3 py-1 md:py-0 transition-all duration-300 uppercase ease-in-out text-lg cursor-pointer text-gray-300 hover:text-gray-500">
                  home
                </div>
              </a>
              <a href="https://asrg.io/about.html">
                <div className="px-3 py-1 md:py-0 transition-all duration-300 uppercase ease-in-out text-lg cursor-pointer text-gray-300 hover:text-gray-500">
                  about
                </div>
              </a>
              <a href="https://asrg.io/privacy.html">
                <div className="px-3 py-1 md:py-0 transition-all duration-300 uppercase ease-in-out text-lg cursor-pointer text-gray-300 hover:text-gray-500">
                  data privacy
                </div>
              </a>

              <a href="https://asrg.io/imprint.html">
                <div className="px-3 py-1 md:py-0 transition-all duration-300 uppercase ease-in-out text-lg cursor-pointer text-gray-300 hover:text-gray-500">
                  imprint
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

const Icon = ({ link, icon }) => (
  <a href={link}>
    <i
      className={
        "text-xl transition-colors duration-300 ease-in-out cursor-pointer text-gray-300 hover:text-gray-500 fa fa-" +
        icon
      }
    ></i>
  </a>
);

export default App;
