import React from 'react'
import NavBar from '../Components/NavBar'
import { Outlet } from 'react-router-dom'

function MainLayout() {
  return (
    <div>
    <NavBar/>

    <Outlet/>
    </div>
  )
}

export default MainLayout
