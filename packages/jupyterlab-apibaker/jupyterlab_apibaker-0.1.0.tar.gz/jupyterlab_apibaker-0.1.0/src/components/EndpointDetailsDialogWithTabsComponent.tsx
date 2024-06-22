import React from 'react';
import { CssBaseline, Box, Tab, Dialog, DialogTitle, DialogContent, DialogActions, Button } from '@mui/material';
import { TabList, TabContext, TabPanel } from '@mui/lab';
import EndpointSummary from './EndpointSummaryComponent';
import { IEndpoint } from '../common/types';
import EndpointAPIKeyComponent from './EndpointAPIKeyComponent';
import EndpointLogs from './EndpointLogsComponent';

interface IEndpointDetailsProps {
     open: boolean
     endpoint: IEndpoint
     handleClose: () => void
}

const EndpointDetailsDialogWithTabs: React.FC<IEndpointDetailsProps> = (props): JSX.Element => {
     const [value, setValue] = React.useState('1');

     const handleChange = (event: React.SyntheticEvent, newValue: string) => {
          setValue(newValue);
     };
     return (
          <React.Fragment>
               <CssBaseline />
               <Dialog
                    sx={{ '& .MuiDialog-paper': { maxHeight: '70%' } }}
                    onClose={props.handleClose}
                    open={props.open}
                    fullWidth={true}
                    maxWidth='lg'
               >
                    <DialogTitle>Endpoint Details</DialogTitle>
                    <DialogContent sx={{ height: '100vh' }} >
                         <Box sx={{ width: '100%', typography: 'body1' }} >
                              <TabContext value={value}>
                                   <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                                        <TabList onChange={handleChange} aria-label="lab API tabs example" variant='fullWidth'>
                                             <Tab label="Summary" value="1" />
                                             <Tab label="API Keys" value="2" />
                                             <Tab label="Logs" value="3" />
                                             <Tab label="Analytics" value="4" />
                                        </TabList>
                                   </Box>
                                   <TabPanel value="1"><EndpointSummary endpoint={props.endpoint} /></TabPanel>
                                   <TabPanel value="2"><EndpointAPIKeyComponent {...props.endpoint} /></TabPanel>
                                   <TabPanel value="3"><EndpointLogs endpoint={props.endpoint} /></TabPanel>
                              </TabContext>
                         </Box>
                    </DialogContent>
                    <DialogActions>
                         <Box sx={{
                              display: 'flex',
                              flexDirection: 'row',
                              justifyContent: 'flex-end',
                              alignItems: 'center',
                              alignContent: 'center',
                              width: '100%'
                         }}>
                              <Button variant='text' sx={{ mr: 1 }}>Open notebook</Button>
                              <Button variant='text' onClick={props.handleClose}>Close</Button>
                         </Box>
                    </DialogActions>
               </Dialog>
          </React.Fragment >
     )
};

export default EndpointDetailsDialogWithTabs;
