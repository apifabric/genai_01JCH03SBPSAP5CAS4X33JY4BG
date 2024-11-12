import { MenuRootItem } from 'ontimize-web-ngx';

import { AppointmentCardComponent } from './Appointment-card/Appointment-card.component';

import { AttendanceCardComponent } from './Attendance-card/Attendance-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { EventCardComponent } from './Event-card/Event-card.component';

import { FeedbackCardComponent } from './Feedback-card/Feedback-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderItemCardComponent } from './OrderItem-card/OrderItem-card.component';

import { PetCardComponent } from './Pet-card/Pet-card.component';

import { ScheduleCardComponent } from './Schedule-card/Schedule-card.component';

import { StaffCardComponent } from './Staff-card/Staff-card.component';

import { StockCardComponent } from './Stock-card/Stock-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Appointment', name: 'APPOINTMENT', icon: 'view_list', route: '/main/Appointment' }
    
        ,{ id: 'Attendance', name: 'ATTENDANCE', icon: 'view_list', route: '/main/Attendance' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Event', name: 'EVENT', icon: 'view_list', route: '/main/Event' }
    
        ,{ id: 'Feedback', name: 'FEEDBACK', icon: 'view_list', route: '/main/Feedback' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderItem', name: 'ORDERITEM', icon: 'view_list', route: '/main/OrderItem' }
    
        ,{ id: 'Pet', name: 'PET', icon: 'view_list', route: '/main/Pet' }
    
        ,{ id: 'Schedule', name: 'SCHEDULE', icon: 'view_list', route: '/main/Schedule' }
    
        ,{ id: 'Staff', name: 'STAFF', icon: 'view_list', route: '/main/Staff' }
    
        ,{ id: 'Stock', name: 'STOCK', icon: 'view_list', route: '/main/Stock' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AppointmentCardComponent

    ,AttendanceCardComponent

    ,CustomerCardComponent

    ,EventCardComponent

    ,FeedbackCardComponent

    ,OrderCardComponent

    ,OrderItemCardComponent

    ,PetCardComponent

    ,ScheduleCardComponent

    ,StaffCardComponent

    ,StockCardComponent

    ,SupplierCardComponent

];